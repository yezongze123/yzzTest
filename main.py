# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections
import sys
import torch
import numpy as np
import math
from functools import reduce
import time  # 引入time模块
from flask import Flask
'''
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    list1 = list(map(int, line.split()))

if __name__ == "__main__":
    # !/usr/bin/env python3
    # -*- coding: utf-8 -*-

    import functools
    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(wrapper.__name__)
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    @log
    def now():
        print('2015-3-25')
    now()

    def logger(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    @logger('DEBUG')
    def today():
        print('2015-3-25')

    today()
    print(today.__name__)
'''
print(torch.__version__)




