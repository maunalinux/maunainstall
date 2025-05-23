#!/usr/bin/python3

import os
import time

from gi.repository import Gio

DEBUG_MODE = os.getenv("DEBUG", False)

# Used as a decorator to time functions
def print_timing(func):
    if not DEBUG_MODE:
        return func
    else:
        def wrapper(*arg):
            t1 = time.time()
            res = func(*arg)
            t2 = time.time()
            print('%s took %0.3f ms' % (func.__qualname__, (t2 - t1) * 1000.0))
            return res
        return wrapper

def debug(str):
    if not DEBUG_MODE:
        return
    print("Maunainstall (DEBUG): %s" % str)

def networking_available():
    nm = Gio.NetworkMonitor.get_default()
    return nm.get_connectivity() == Gio.NetworkConnectivity.FULL
