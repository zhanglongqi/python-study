__author__ = 'longqi'

import sched
import time
from pymodbus.client.sync import ModbusTcpClient
import pymodbus

requestScheduler = sched.scheduler(time.time, time.sleep)
modbusClient = ModbusTcpClient('192.168.0.10')

# bi-directional converter configuration
bidirecRegs = []
bidirecRegsReadInter = 0.5
bidirecRegsReadPriority = 1
bidirecRegsStartAddr = 11025
bidirecRegsNo = 20


def read_data_bidirec():
    #Bi-directional converter
    try:
        res = modbusClient.read_holding_registers(bidirecRegsStartAddr, bidirecRegsNo)
        global bidirecRegs
        bidirecRegs = res.registers
    except pymodbus.exceptions.ConnectionException:
        print 'Communication faild...'

    if len(bidirecRegs) == bidirecRegsNo:
        print 'Reading success...'


def setup_timer():
    requestScheduler.enter(bidirecRegsReadInter, bidirecRegsReadPriority, read_data_bidirec, ())
    #requestScheduler.enter(0.5, 1, read_data, ())
    requestScheduler.run()


def start_data_server():
    print 'startting timer ...'
    setup_timer()


if __name__ == "__main__":
    start_data_server()