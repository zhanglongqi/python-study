__author__ = 'longqi'

import socket


def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]


# print((getNetworkIp()))

'''

############################
'''

print(([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in
        [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]))

'''

############################
'''
import sys

if sys.version_info.major < 2:
    raise RuntimeError('Python 2.7 And Above Only')

from subprocess import check_output  # Available on Python 2.7+ | N/A

print(check_output(['ip', 'route']).splitlines())
