#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by longqi on 9/11/14
"""
__author__ = 'longqi'
'''
print('*****************************')

from threading import Thread
from time import sleep


def threaded_function(arg):
    for i in range(arg):
        print(("running", arg))
        sleep(1)


if __name__ == "__main__":
    # thread1 = Thread(target=threaded_function, args=(10, ))
    # thread1.start()

    # thread2 = Thread(target=threaded_function, args=(20, ))
    # thread2.start()

    for i in range(1, 3):
        new_thread = Thread(target=threaded_function, args=(i, ))
        new_thread.start()
    new_thread.join()
    print("thread finished...exiting")

'''

from threading import Thread
from time import sleep
import logging


class FileParserBase():
    def __init__(self, target=None):
        # logging setting

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        self.log_h = logging.StreamHandler()
        # log_h = logging.FileHandler('log.log')
        self.log_h.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        self.log_h.setFormatter(self.formatter)
        self.logger.addHandler(self.log_h)

        self.target = target
        self.data_model = None

        self.new_last_pos = 0


class FileParser(FileParserBase):
    def __init__(self, target):
        self.count = 0
        self.count += 1
        FileParserBase.__init__(self, target=target)
        self.logger.info('parsing file' + str(self.count))
        print('parsing file' + str(self.count))

    def process(self):
        self.count += 1
        self.logger.info(self.target + '\t' + 'deal finished***************' + str(self.count))
        print(self.target + '\t' + 'deal finished***************' + str(self.count))

    def __del__(self):
        print('byebye')


class TEST():
    def __init__(self, var):
        print('\n\nHi  ' + var)

    def __del__(self):
        print('BYE  ')


def foo(var):
    test = TEST(var)
    new_file_parser = FileParser('file_path')
    new_file_parser.process()


i = 1
while True:
    i += 1
    new_thread = Thread(target=foo, args=(str(i),))
    new_thread.start()
    new_thread.join()
    sleep(1)
