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
            while buf != '-1':
                if buf == '1':
                    connection.send('welcome to server! 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1')
                elif buf == '2':
                    connection.send('welcome to server! 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2')
                elif buf == '-1':
                    connection.send('Disconnecting...')
                    connection.close()
                buf = connection.recv(4096)
        except socket.timeout:
            print 'time out'
            connection.close()