from serial import Serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time

master = modbus_rtu.RtuMaster(Serial(port='/dev/ttyUSB0', baudrate=19200, bytesize=8, parity='N', stopbits=1))
master.set_timeout(1)
master.set_verbose(True)

#get etica pack data 
try:
    for i in range(1, 5):
        red = master.execute(i, cst.READ_HOLDING_REGISTERS, 10, 5)
        print(red)
        time.sleep(1)
except Exception as ex:
    print(f'error: {str(ex)}')