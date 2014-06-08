import mmap
import sched
import time

from pymodbus.client.sync import ModbusTcpClient
import pymodbus


class DevBase(object):
    def __init__(self):

        # device info
        self.summary = ''
        self.regs = []

        # data sharing info
        self.f = open("regs_bid.dat", "r+")
        self.mmapData = mmap.mmap(self.f.fileno(), 0)

        # devices registers info
        self.regsReadInter = 0.5
        self.regsReadPriority = 1
        self.regsStartAddr = 11025
        self.regsNo = 20

        # devices address info
        self.modbusClient = ModbusTcpClient('192.168.0.10')
        self.requestScheduler = sched.scheduler(time.time, time.sleep)

    def delete_from_mmap(self, start, end):

        length = end - start
        size = len(self.mmapData)
        newsize = size - length

        self.mmapData.move(start, end, size - end)
        self.mmapData.flush()
        self.mmapData.close()
        self.f.truncate(newsize)
        self.mmapData = mmap.mmap(self.f.fileno(), 0)

    def insert_into_mmap(self, offset, data):

        length = len(data)
        size = len(self.mmapData)
        newsize = size + length

        self.mmapData.flush()
        self.mmapData.close()
        self.f.seek(size)
        self.f.write("A" * length)
        self.f.flush()
        self.mmapData = mmap.mmap(self.f.fileno(), 0)
        self.mmapData.move(offset + length, offset, size - offset)
        self.mmapData.seek(offset)
        self.mmapData.write(data)
        self.mmapData.flush()

    def replace_in_mmap(self, offset, olddata, newdata):

        self.insert_into_mmap(offset, newdata)
        self.delete_from_mmap(offset + len(newdata), offset + len(newdata) + len(olddata))

    def read_data(self):
        try:
            res = self.modbusClient.read_holding_registers(self.regsStartAddr, self.regsNo)
            self.regs = res.registers
        except pymodbus.exceptions.ConnectionException:
            print 'Communication faild...'

        if len(self.regs) == self.regsNo:
            print 'Reading success...'

    def setup_timer(self):
        self.requestScheduler.enter(self.regsReadInter, self.regsReadPriority, self.read_data, ())
        # requestScheduler.enter(0.5, 1, read_data, ())
        self.requestScheduler.run()

    def start_data_server(self):
        print 'startting timer ...'
        self.setup_timer(self)