import sys
import os
from keyed_file import KeyedFile

KEYED_BLOCK_SIZE = 512
FILE_SIZE = 0
# Random file: Fixed length records delimited by newlines
# Sequential: Variable length records delimited by newlines
# Direct: Records one after another without any delimiter or new lines

# Check if file is provided as argument
if len(sys.argv) != 2:
    quit('Usage: file <filename>')

# Check if file exists
if not os.path.isfile(sys.argv[1]):
    quit('File does not exist')

# Check if file is empty
FILE_SIZE = os.path.getsize(sys.argv[1])
if FILE_SIZE == 0:
    print('Empty file')
    quit(0)


def is_keyed():
    kfile = KeyedFile()
    # Check if file size is multiple of 512
    if FILE_SIZE % KEYED_BLOCK_SIZE:
        return

    with open(sys.argv[1], 'rb') as f:
        control_block = f.read(KEYED_BLOCK_SIZE)
        kfile.og_file_name = control_block[12:30]

        year = control_block[30] | control_block[31] << 8
        month = control_block[32]
        day = control_block[33]
        kfile.creation_date = '{}-{}-{}'.format(year, month, day)

        kfile.blocks_qty = control_block[42] | \
                        (control_block[43] << 8) | \
                        (control_block[44] << 16) | \
                        (control_block[45] << 24)
        kfile.key_length = control_block[54] | (control_block[55] << 8)
        kfile.record_size = control_block[46] | (control_block[47] << 8)

        if kfile.blocks_qty * KEYED_BLOCK_SIZE != FILE_SIZE:
            return
        print('Keyed file')
        quit(0)


is_keyed()

with open(sys.argv[1], 'rb') as f:
    lines = f.readlines()
    f.seek(0)

    if len(lines) == 1:
        print('Direct file')
        quit(0)
    else:
        is_direct = False
        for line in lines:
            if line[-2:] == b'\x00\n':
                is_direct = True
            elif line[-2:] == b'\r\n':
                is_direct = False
                break
        if is_direct:
            print('Direct file')
            quit(0)

with open(sys.argv[1], 'rb') as f:
    is_random = False
    first_line_length = len(f.readline())

    for line in f:
        if first_line_length == len(line):
            is_random = True
        else:
            is_random = False
            break

    if is_random:
        print('Random file')
        quit(0)
    else:
        print('Sequential file')
