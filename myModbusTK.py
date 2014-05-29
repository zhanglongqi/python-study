__author__ = 'longqi'
import modbus_tk
import modbus_tk.modbus_tcp

master = modbus_tk.modbus_tcp.TcpMaster('192.168.0.101')
master.set_timeout(2)

res = master.execute(2, modbus_tk.defines.READ_HOLDING_REGISTERS, 3999, 24)
print res
