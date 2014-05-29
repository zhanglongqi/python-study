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

import sched, time

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