#!usr/bin/env python3
from chardet import detect
import sys

def char_type(filepath):
    with open(filepath, 'rb') as f:
        result = detect(f.read())
    return result['encoding']

def run():
    filepath = sys.argv[0]
    # result = char_type(filepath)
    # print(f"The ")
    print(filepath)
    
if __name__ == '__main__':
    run()