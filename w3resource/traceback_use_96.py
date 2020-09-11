import traceback


def abc():
    traceback.print_stack()


def func():
    abc()


func()
#   File "F:/projects/python/w3resource/traceback_use_96.py", line 12, in <module>
#     func()
#   File "F:/projects/python/w3resource/traceback_use_96.py", line 9, in func
#     abc()
#   File "F:/projects/python/w3resource/traceback_use_96.py", line 5, in abc
#     traceback.print_stack()
