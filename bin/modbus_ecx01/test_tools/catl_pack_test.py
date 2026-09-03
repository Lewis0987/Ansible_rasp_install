from serial import Serial
import time
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import modbus_tk.hooks as hooks

from dataset import DataMap
from api_upload import upload_data, upload_alert

class SLF01_Uploader():
    def calc_crc(self, data):
        crc = 0xFFFF
        for pos in data:
            crc ^= pos 
            for i in range(8):
                if ((crc & 1) != 0):
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return crc

    def fix_catl_modbus(self, args):
        """修正CATL儲能電池非正規的Modbus"""
        fixed_data = args[1]
        #刪除多餘的Length Byte
        del fixed_data[2]
        #刪除CRC LSB
        del fixed_data[-1]
        #修正長度
        fixed_data[2] *= 2
        #重新計算CRC
        crc_MSB = (0xFF00 & self.calc_crc(args[1])) >> 8
        crc_LSB = (0x00FF & self.calc_crc(args[1]))
        #把CRC加回修正後的data
        fixed_data.append(crc_LSB)
        fixed_data.append(crc_MSB)
        return fixed_data

    try:
        #hooks.install_hook("modbus_rtu.RtuMaster.after_recv", self.fix_catl_modbus)
        pass
    except:
        pass
    red = []
    try:
        master = modbus_rtu.RtuMaster(Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1))
        master.set_timeout(5)
        master.set_verbose(True)

        #Get 中能 Pack data
        red = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 1)
        print(red)

    except Exception as exc:
        print("error",str(exc))
