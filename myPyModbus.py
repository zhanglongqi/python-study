__author__ = 'longqi'
#import pymodbus

#print pymodbus
#rHR = pymodbus.register_read_message.ReadHoldingRegistersRequest()

import time
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')

'''
regNo = 20
costtime = []
j = 10
while j:

    lasttime = time.time()
    res = client.read_holding_registers(11025, regNo)
    thistime = time.time()

    print res.registers, '\n'
    costtime.append(thistime - lasttime)
    j -= 1

print 'Avergage time of reading 20 register: ', sum(costtime) / len(costtime)
'''

'''
#res = client.read_coils(409, 1)
#client.write_coil(413, False)
#print res.bits, '\n'
j = 10
#while False:
#while j:
#    client.write_coils(100, [False]*6)
#    client.write_coils(200, [False]*6)
#    client.write_coils(300, [False]*6)
#    client.write_coils(400, [False]*6)
#    client.write_coils(500, [False]*6)
#    client.write_coils(600, [False]*6)
#    client.write_coils(700, [False]*6)
#    client.write_coils(800, [False]*6)
    time.sleep(1)
#    client.write_coils(100, [True]*6)
#    client.write_coils(200, [True]*6)
#    client.write_coils(300, [True]*6)
#    client.write_coils(400, [True]*6)
#    client.write_coils(500, [True]*6)
#    client.write_coils(600, [True]*6)
#    client.write_coils(700, [True]*6)
#    client.write_coils(800, [True]*6)
    time.sleep(1)
    j -= 1


res = client.read_coils(701, 8)
print res.bits
res = client.read_coils(709, 8)
print res.bits, '\n'

client.write_coil(701, True)
client.write_coil(703, True)

#client.write_coils(700, [False]*8)
res = client.read_coils(701, 8)
print res.bits
res = client.read_coils(709, 8)
print res.bits
'''

t1 = time.time()
res = client.read_holding_registers(10985, 20, unit=1)
t2 = time.time()
print res.registers, '\n', t2 - t1