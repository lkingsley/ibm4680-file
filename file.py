import sys
import os
from util import is_direct, is_empty, is_keyed, is_random

# Direct file: Records one after another without any delimiter or new lines
# Keyed file: Fixed length records with a control block at the beginning
#             of the file
# Random file: Fixed length records delimited by CR/LF
# Sequential file: Variable length records delimited by CR/LF

if __name__ == '__main__':
    if len(sys.argv) != 2:
        quit('Usage: file.py <filename>')

    file_name = sys.argv[1]
    
    if not os.path.isfile(file_name):
        quit('File does not exist')

    is_empty(file_name)
    is_keyed(file_name)
    is_direct(file_name)
    is_random(file_name)
    
    print('Sequential file')
