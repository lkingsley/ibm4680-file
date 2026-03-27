import sys
import os
from util import is_direct, is_empty, is_keyed, is_random

if __name__ == '__main__':
    if len(sys.argv) != 2:
        quit('Usage: file.py <filename>')

    file_name = sys.argv[1]

    if not os.path.isfile(file_name):
        print('%s: No such file or directory' % file_name)
        quit(1)

    is_empty(file_name)
    is_keyed(file_name)
    is_direct(file_name)
    is_random(file_name)

    print('Sequential file')
