import sys
from python.python_cook.module_all_test import *
import pkgutil

# print(globals())
#
# lis = [1, 2, 3]
# lis.extend((4, 5))
# print(lis)

# data = pkgutil.get_data('python_cook', 'somedata.dat')
# print(data)

import importlib


test = importlib.import_module('module_all_test')
test.spam()

