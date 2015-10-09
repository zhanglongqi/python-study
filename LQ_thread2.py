#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by longqi on 10/23/14
"""
__author__ = 'longqi'

from threading import Thread
from threading import Event
from time import sleep


class ThreadTest(Thread):
    def __init__(self, nap_time):
        Thread.__init__(self)
        self.exit_event = Event()
        self.nap_time = nap_time
        self.times_ran = 0
        self.start()

    def exit(self, wait_for_exit=False):
        print("Thread asked to exit, messaging run")
        self.exit_event.set()
        if wait_for_exit:
            print("Thread exit about to wait for run to finish")
            self.join()
        return self.report()

    def run(self):
        while not self.exit_event.isSet():
            self.times_ran += 1
            print("Thread running iteration", self.times_ran)
            sleep(self.nap_time)
        print("Thread run received exit event")

    def report(self):
        if self.is_alive():
            return "Status:  I'm still alive"
        else:
            return "Status:  I'm dead after running %d times" % self.times_ran


def tester(wait_for_exit=False):
    print("Starting test; wait for exit:", wait_for_exit)
    t = ThreadTest(0.5)
    sleep(1)
    print(t.report())  # Still alive here
    sleep(2)
    print("Main about to ask thread to exit")
    e = t.exit(wait_for_exit)  # let the child thread exit,the difference here is whether to wait it
    print("Exit call report:", e)
    sleep(1)
    print(t.report())  # Thread is certainly done by now


if __name__ == '__main__':
    tester(False)
    print()
    tester(True)
