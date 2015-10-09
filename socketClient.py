__author__ = 'longqi'

if __name__ == '__main__':
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    import time

    sock.send(bytes('1', encoding='utf8'))
    t1 = time.time()
    res = sock.recv(1024)
    t2 = time.time()
    print(res, '\n', t2 - t1)

    sock.send(bytes('2', encoding='utf8'))
    res = sock.recv(1024)
    print(res)

    sock.send(bytes('-1', encoding='utf8'))
    res = sock.recv(1024)
    print(res)

    sock.close()
