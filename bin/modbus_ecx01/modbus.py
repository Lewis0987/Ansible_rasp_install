from serial import Serial
import time
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
from _thread import *

from dataset import DataMap
from api_upload_catl import upload_data, upload_alert
from api_upload_inv_only import upload_data as upload_data_inv_only
class ECX01_Uploader():
    def __init__(self) -> None:
        self.flag_sync_inv = False
        self.flag_sync_pack = False

    def mod_inv(self, datamap, PORT="/dev/ttyUSB0"):
        '''
        try:
            hooks.uninstall_hook("modbus_rtu.RtuMaster.after_recv")
        except:
            pass
        '''
        red = []
        try:      
            master = modbus_rtu.RtuMaster(Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1))
            master.set_timeout(1)
            master.set_verbose(True)

            #Get URVOLT Inverter data 
            for name, data in datamap.Inverter.items():
                try:
                    red = master.execute(1, cst.READ_HOLDING_REGISTERS, data.start_address, data.end_address - data.start_address + 1)
                    data.setval(red)
                    print(f'Target: Inverter, Name: {name}, {hex(data.start_address).upper()}, {hex(data.end_address).upper()}, Value: {data.val_hex().upper()}')
                except Exception as ex:
                    print(f'Target: Inverter, Name: {name}, {hex(data.start_address).upper()}, {hex(data.end_address).upper()}, error: {str(ex)}')
                    return False
            self.flag_sync_inv= True
        except Exception as exc:
            print("error",str(exc))
            self.flag_sync_inv = False
            return False

        return True

    def mod_catl_pack(self, datamap, PORT="/dev/ttyUSB1"):
        '''
        try:
            pass
            hooks.install_hook("modbus_rtu.RtuMaster.after_recv", self.fix_catl_modbus)
        except:
            pass
        '''
        red = []
        try:
            master = modbus_rtu.RtuMaster(Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1))
            master.set_timeout(5)
            master.set_verbose(True)

            #Get 中能 Pack data
            for i in range(4):
                for name, data in datamap.Packs[i].items():
                    try:
                        red = master.execute(i + 1, cst.READ_HOLDING_REGISTERS, data.start_address, data.end_address - data.start_address + 1)
                        print(red)
                        data.setval(red)
                        print(f'Target: Pack{i + 1}, Name: {name}, {hex(data.start_address).upper()}, {hex(data.end_address).upper()}, Value: {data.val_hex().upper()}')
                    except Exception as ex:
                        print(f'Target: Pack{i + 1}, Name: {name}, {hex(data.start_address).upper()}, {hex(data.end_address).upper()}, error: {str(ex)}')
                        return False
                time.sleep(1)
            self.flag_sync_pack= True

        except Exception as exc:
            print("error",str(exc))
            self.flag_sync_pack = False
            return False

        return True

    def mod_etica_pack(self, datamap, PORT="/dev/ttyUSB0"):
        '''
        try:
            hooks.uninstall_hook("modbus_rtu.RtuMaster.after_recv")
        except:
            pass
        '''
        try:
            master = modbus_rtu.RtuMaster(Serial(port=PORT, baudrate=19200, bytesize=8, parity='N', stopbits=1))
            master.set_timeout(5)
            master.set_verbose(True)

            #Get 明曜 Pack data
            for i in range(0, 4):
                for name, data in datamap.Packs[i].items():
                    try:
                        red = master.execute(i + 1, cst.READ_HOLDING_REGISTERS, data.start_address, data.end_address - data.start_address + 1)
                        print(red)
                        data.setval(red)
                        print(f'Target: Pack{i + 1}, Name: {name}, {hex(data.start_address).upper()}, {hex(data.end_address).upper()}, Value: {data.val_hex().upper()}')
                    except Exception as ex:
                        print(f'Target: Pack{i + 1}, Name: {name}, {hex(data.start_address).upper()}, {hex(data.end_address).upper()}, error: {str(ex)}')
                        return False
                time.sleep(1)
            self.flag_sync_pack= True
                    
        except Exception as exc:
            print("error",str(exc))
            self.flag_sync_pack = False
            return False

        return True

    def loop_mod_inv(self, datamap):
        while True:
            if self.mod_inv(datamap, PORT='/dev/inverter') == False:
                time.sleep(1)

    def loop_mod_pack(self, datamap):
        while True:
            if self.mod_catl_pack(datamap, PORT='/dev/bms') == False:
                time.sleep(1)

    def run(self):
        datamap = DataMap()
        time_start = time.time()
        time_end = time.time()
        trigger_error = False

        #確保執行過初次的通訊
        self.mod_inv(datamap, PORT='/dev/inverter')
        self.mod_catl_pack(datamap, PORT='/dev/bms')

        #後台執行polling
        start_new_thread(self.loop_mod_inv, (datamap, ))
        start_new_thread(self.loop_mod_pack, (datamap, ))
        
        while(True):
            time_start = time.time()
            if self.flag_sync_inv == True and self.flag_sync_pack == True:
                upload_data(datamap, time_end)
                trigger_error = False
            else:
                if trigger_error is False:
                    upload_alert('comm failed')
                    trigger_error = True
                #Pack讀不到但Inverter有讀到的情況處理
                if self.flag_sync_inv == True:
                    upload_data_inv_only(datamap, time_end)

            time_end = time.time()
            print(f'elapse time: {time_end - time_start}')
            time.sleep(5)

if __name__ == "__main__":
    uploader = ECX01_Uploader()
    uploader.run()