import sys
import os

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
if os.path.getsize(sys.argv[1]) == 0:
    print('Empty file')
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
