# countdown.py
#
# An example of defining a thread as a class

import time
import threading


class CountdownThread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            # print "Counting down", self.count
            self.count -= 1
        # time.sleep(5)
        return

# Sample execution
t1 = CountdownThread(10000000000)
t2 = CountdownThread(20000000000)

t1.start()
t2.start()

while t1.is_alive() or t2.is_alive():
    time.sleep(0.01)
print 'done'