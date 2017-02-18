# TODO: FOCUS ON THIS TECHNIQUE FOR STREAMING IMAGES

import time
import os

total_bytes = os.path.getsize('sometextfile.txt')
iterator = 0
string_buffer = ''
file1 = open('sometextfile.txt', 'rb')

def ingestFakeStream(char):
    if char != ';':
        global string_buffer
        string_buffer += char
    else:
        print 'parsed nibble: ' + string_buffer
        string_buffer = ''

def main():
    while iterator < total_bytes:
        ingestFakeStream(file1.read(1))
        time.sleep(0.005)

if __name__ == "__main__":
    main()