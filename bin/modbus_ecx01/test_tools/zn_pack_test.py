from serial import Serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time

master = modbus_rtu.RtuMaster(Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1))
master.set_timeout(1)
master.set_verbose(True)

#get zhongnen pack data 
try:
    watt_sum = 0
    for i in range(1, 5):
        red = master.execute(i, cst.READ_HOLDING_REGISTERS, 0x31, 2)
        watt = red[0] * red[1] * 0.01
        print(watt)
        watt_sum+= watt

        temp = master.execute(i, cst.READ_HOLDING_REGISTERS, 0x26, 1)
        print((temp[0] *0.1) - 273)
        time.sleep(0.5)
    print(f'Total {watt_sum}')
except Exception as ex:
    print(f'error: {str(ex)}')