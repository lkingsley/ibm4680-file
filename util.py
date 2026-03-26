import os
import re
from keyed_file import KeyedFile, BLOCK_SIZE


def hex_to_int(hex_string):
    return int(hex_string.encode('hex'), 16)


def is_direct(file_name):
    with open(file_name, 'rb') as f:
        match = re.search(b'\r\n', f.read())
        if match is None:
            print('Direct file')
            quit(0)


def is_empty(file_name):
    if os.path.getsize(file_name) == 0:
        print('Empty file')
        quit(0)


def is_keyed(file_name):
    kfile = KeyedFile()
    file_size = os.path.getsize(file_name)

    # Stop function if file size is not multiple of 512
    if file_size % BLOCK_SIZE:
        return

    with open(file_name, 'rb') as f:
        control_block = f.read(BLOCK_SIZE)
        kfile.og_file_name = control_block[12:30].decode(
            encoding='utf-8', errors='ignore').rstrip('\x00')
                                    
        year = hex_to_int(control_block[30]) | (hex_to_int(control_block[31]) << 8)
        month = hex_to_int(control_block[32])
        day = hex_to_int(control_block[33])
        kfile.creation_date = '{}/{}/{}'.format(year, month, day)
        
        kfile.blocks_qty = hex_to_int(control_block[42]) | (hex_to_int(control_block[43]) << 8) | \
            (hex_to_int(control_block[44]) << 16) | \
            (hex_to_int(control_block[45]) << 24)
        kfile.key_length = hex_to_int(control_block[54]) | (hex_to_int(control_block[55]) << 8)
        kfile.record_size = hex_to_int(control_block[46]) | (hex_to_int(control_block[47]) << 8)

        if kfile.blocks_qty * BLOCK_SIZE != file_size:
            return
        print('Keyed file')
        quit(0)


def is_random(file_name):
    with open(file_name, 'rb') as f:
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
