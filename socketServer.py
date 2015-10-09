__author__ = 'longqi'
if __name__ == '__main__':
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8001))
    sock.listen(5)
    '''
    Listen for connections made to the socket. The backlog argument specifies the maximum number of queued connections
    and should be at least 0; the maximum value is system-dependent (usually 5), the minimum value is forced to 0.
    '''
    while True:
        connection, address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(4096)
            buf = str(buf, encoding='utf-8')
            while True:
                if buf == '1':
                    connection.send(bytes('welcome to server! 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1', encoding='utf8'))
                elif buf == '2':
                    connection.send(bytes('welcome to server! 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2', encoding='utf8'))
                elif buf == '-1':
                    connection.send(bytes('Disconnecting...', encoding='utf8'))

                    connection.close()
                    break;

                buf = connection.recv(4096)
                buf = str(buf, encoding='utf-8')

        except socket.timeout:
            print('time out')
            connection.close()

    sock.close()
