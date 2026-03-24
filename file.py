import sys
import os
from keyed_file import KeyedFile

KEYED_BLOCK_SIZE = 512
FILE_SIZE = 0
# Random file: fixed length records delimited by newlines
# Sequential: variable length records delimited by newlines
# Direct: Data one after another without any delimiter

# TODO:1. check if file is keyed
# TODO:2. check if file has only one line


# Check if file is provided as argument
if len(sys.argv) != 2:
    quit('Usage: file <filename>')

# Check if file exists
if not os.path.isfile(sys.argv[1]):
    quit('File does not exist')

# Check if file is empty
FILE_SIZE = os.path.getsize(sys.argv[1])
if FILE_SIZE == 0:
    quit('Empty file')

def is_keyed():
    kfile = KeyedFile()
    if FILE_SIZE % KEYED_BLOCK_SIZE:
        print('not multiple')
    with open(sys.argv[1], 'rb') as f:
        first_block = f.read(512)
        kfile.og_file_name = first_block[12:30]

        year = first_block[30] | first_block[31] << 8
        month = first_block[32]
        day = first_block[33]
        kfile.creation_date = '{}-{}-{}'.format(year, month, day)
        
        kfile.blocks_qty = first_block[42] | \
                        (first_block[43] << 8) | \
                        (first_block[44] << 16) | \
                        (first_block[45] << 24)
        kfile.key_length = first_block[54] | (first_block[55] << 8)
        kfile.record_size = first_block[46] | (first_block[47] << 8)
        kfile.print()
# TODO: finish keyed file validation
is_keyed()
quit(0)

with open(sys.argv[1], 'rb') as f:
    if len(f.readlines()) == 1:
        print('Direct file')
        quit(0)


with open(sys.argv[1], 'rb') as f:
    first_line_length = len(f.readline())
    is_random = False
    for line in f:
        if first_line_length == len(line):
            is_random = True
        else:
            is_random = False
            break
    if is_random:
        print('Random file')
        quit()
    else:
        print('Sequential file')
        quit(0)
