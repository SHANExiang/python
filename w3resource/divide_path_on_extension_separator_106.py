

def divide_path_on_extension_separator():
    import os.path
    for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
        print('"%s" :' % path, os.path.splitext(path))


divide_path_on_extension_separator()
# "test.txt" : ('test', '.txt')
# "filename" : ('filename', '')
# "/user/system/test.txt" : ('/user/system/test', '.txt')
# "/" : ('/', '')
# "" : ('', '')
