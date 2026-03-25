import sys
import os
from util import is_direct, is_keyed, is_random

# Direct file: Records one after another without any delimiter or new lines
# Keyed file: Fixed length records with a control block at the beginning
#             of the file
# Random file: Fixed length records delimited by CR/LF
# Sequential file: Variable length records delimited by CR/LF

# Check if file is provided as argument
if len(sys.argv) != 2:
    quit('Usage: file.py <filename>')

# Check if file exists
if not os.path.isfile(sys.argv[1]):
    quit('File does not exist')

# Check for empty file
if os.path.getsize(sys.argv[1]) == 0:
    print('Empty file')
    quit(0)


is_keyed(sys.argv[1])

is_direct(sys.argv[1])

is_random(sys.argv[1])

print('Sequential file')
