__author__ = 'longqi'
import subprocess
import time

ip = '155.69.227.252'
timeInter = 30


def check_net_ok(target):
    res = subprocess.call("ping -c 1 %s" % target, shell=True, stdout=open('/dev/null', 'w'),
                          stderr=subprocess.STDOUT)

    if res != 0:
        res = subprocess.call("ping -c 1 %s" % target, shell=True, stdout=open('/dev/null', 'w'),
                              stderr=subprocess.STDOUT)

    if res != 0:
        res = subprocess.call("ping -c 1 %s" % target, shell=True, stdout=open('/dev/null', 'w'),
                              stderr=subprocess.STDOUT)

    if res == 0:
        return True
    else:
        return False


while True:
    time.sleep(timeInter)
    if check_net_ok(ip):
        print(time.time(), 'network is OK...\n')
    else:
        print(time.time(), 'restart network... \n')
        subprocess.call("/sbin/ifup wlan0", shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
