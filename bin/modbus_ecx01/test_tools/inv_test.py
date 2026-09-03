from serial import Serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time

master = modbus_rtu.RtuMaster(Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1))
master.set_timeout(1)
master.set_verbose(True)

#get URVolt pack data 
try:
    

    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x304, output_value = 5650)
    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x305, output_value = 5650)
    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x306, output_value = 5650)
    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x309, output_value = 4700)
    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x30A, output_value = 4700)
    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x30B, output_value = 4700)
    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x30C, output_value = 4700)
    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x30D, output_value = 4700)
    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x300, output_value = 1)

    red = master.execute(1, cst.READ_HOLDING_REGISTERS, 0x300, 14)
    print(red)
    #red = master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x304, output_value = [5650, 5650, 5650])
    #time.sleep(0.5)
    #red = master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 0x309, output_value = [4700, 4700, 4700, 4700, 4700])
    #time.sleep(0.5)
    #red = master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x300, output_value = 1)
    #time.sleep(0.5)
except Exception as ex:
    print(f'error: {str(ex)}')