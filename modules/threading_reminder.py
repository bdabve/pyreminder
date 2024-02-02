#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# /----------------------------------------------------------------------------
#
#          FILE: threadingUse.py
#
#         USAGE: ./threadingUse.py
#
#   DESCRIPTION: theading example from: https://pymotw.com/2/theading
#
#        AUTHOR: daBve (), dabve@outlook.fr
#       CREATED: 12-Jun-2017
#
# \----------------------------------------------------------------------------

import threading
import time

"""
# A multithreaded program has multiple fingers.
# Executing defferent lines of code at the same time.
# Rather than having all of your code wait until the time.sleep() function finishes, you can execute the delayed of sheculed code in a separate thread using Python's threading module
"""

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up!')


threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program')
# Output of this
"""
Start of program.
End of program
Wake up!
"""

# Passing Arguments to the Thread's target function

print('Cats', 'Dogs', 'Frogs', sep=' & ')
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()
# This is wrong
# threadObj = threading.Thread(target=print('Cats', 'Dogs', 'Frogs', sep=' & '))
"""
# You can easily create several new threads and have them all running at the same time. But multiple threads can also cause problems called concurrency issues.
# These issues happen when threads read and write variables at the same time, causing the threads to trip over each other.
# Concurrency issues can be hard to reproduce consistently, making them hard to debug.
# To avoid concurrency issues, never let multiple threads read or write the same variables.
# When you create a new Thread object, make sure its target function uses only local variables in that function.
"""
