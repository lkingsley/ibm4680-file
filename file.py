import sys
import os
from util import is_direct, is_empty, is_keyed, is_random

# Direct file: Records one after another without any delimiter or new lines
# Keyed file: Fixed length records with a control block at the beginning
#             of the file
# Random file: Fixed length records delimited by CR/LF
# Sequential file: Variable length records delimited by CR/LF

# Check if file is provided as argument
if len(sys.argv) != 2:
    quit('Usage: file.py <filename>')

file_name = sys.argv[1]

# Check if file exists
if not os.path.isfile(file_name):
    quit('File does not exist')

is_empty(file_name)
is_keyed(file_name)
is_direct(file_name)
is_random(file_name)

print('Sequential file')
