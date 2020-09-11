

def retrieve_file_properties():
    import os.path
    import time
    print('file is', __file__)
    print('Access time', time.ctime(os.path.getatime(__file__)))
    print('Modify time', time.ctime(os.path.getmtime(__file__)))
    print('create time', time.ctime(os.path.getctime(__file__)))
    print('size of file', os.path.getsize(__file__))


retrieve_file_properties()
# file is F:/projects/python/w3resource/retrieve_file_properties_107.py
# Access time Fri Sep 11 22:59:53 2020
# Modify time Fri Sep 11 22:59:53 2020
# create time Fri Sep 11 22:54:19 2020
# size of file 376
