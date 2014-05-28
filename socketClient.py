__author__ = 'longqi'

if __name__ == '__main__':
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    import time

    sock.send('1')
    t1 = time.time()
    res = sock.recv(1024)
    t2 = time.time()
    print res, t2 - t1

    sock.send('2')
    res = sock.recv(1024)
    print res

    sock.send('-1')

    sock.close()

l1 = {'10': 'print age 10', '20': 'print age 20', '30': 'print 30', 'default': 'print age 10'}

age = '20'
print l1.get(age, 'print age is deault')
age = '21'
print l1.get(age, 'print age is deault')
