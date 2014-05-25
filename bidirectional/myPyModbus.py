__author__ = 'longqi'
#import pymodbus

#print pymodbus
#rHR = pymodbus.register_read_message.ReadHoldingRegistersRequest()

import time
from pymodbus.client.sync import ModbusTcpClient
client = ModbusTcpClient('192.168.0.10')
regNo = 20

costtime = []
j = 1000
while j:

    lasttime = time.time()
    res = client.read_holding_registers(11025, regNo)
    thistime = time.time()
    print res.registers, '\n'
    costtime.append(thistime - lasttime)
    j -= 1

print 'Avergage time of reading 20 register: ', sum(costtime) / len(costtime)

