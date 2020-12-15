import os


def findfile(start_dir, name):
    for relpath, dirs, files in os.walk(start_dir):
        print(relpath, dirs, files)
        if name in files:
            full_path = os.path.join(start_dir, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    findfile('F:/projects/python/', '__init__.py')

