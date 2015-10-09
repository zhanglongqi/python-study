__author__ = 'longqi'
'''
import time
run = raw_input("Start? > ")
mins = 0
# Only run if the user types in "start"
if run == "start":
    # This is saying "while we have not reached 20 minutes running"
    while mins != 20:
        print ">>>>>>>>>>>>>>>>>>>>>", mins
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here
'''

'''
import sched
import time

s = sched.scheduler(time.time, time.sleep)


def print_time():
    print "From print_time", time.time()


def print_some_times():
    print time.time()
    s.enter(5, 1, print_time, ())
    s.enter(10, 1, print_time, ())
    s.run()
    print time.time()


print_some_times()
'''

'''
import sched
import time
def hello(name):
    print 'hello world, i am %s, Current Time:%s' % (name, time.time())
    run(name)

def run(name):
    s = sched.scheduler(time.time, time.sleep)
    s.enter(3, 2, hello, (name,))
    s.run()

s = sched.scheduler(time.time, time.sleep)
s.enter(3, 2, hello, ('guo',))
s.run()

'''

'''
from threading import Event, Thread
import time


class RepeatTimer(Thread):
    def __init__(self, interval, function, iterations=0, args=[], kwargs={}):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.iterations = iterations
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()

    def run(self):
        count = 0
        while not self.finished.is_set() and (self.iterations <= 0 or count < self.iterations):
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
                count += 1

    def cancel(self):
        self.finished.set()

def hello():
    print 'hello world, Current Time:%s' % (time.time())


r = RepeatTimer(5.0, hello)
r.start()
'''

'''
from threading import Timer
def hello():
    print "hello, world"
    t.run()

t = Timer(1.0, hello)
t.start() # after 1 seconds, "hello, world" will be printed
'''

import threading;

i = 0


def work():
    global i
    threading.Timer(0.01, work).start()
    print("stackoverflow ", i, end='\r')
    i += 1


work();
