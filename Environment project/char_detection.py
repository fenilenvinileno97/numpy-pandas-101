#!usr/bin/env python3
from chardet import detect
import sys
import re

def char_type(filepath):
    with open(filepath, 'rb') as f:
        result = detect(f.read())
    return result['encoding']

def pattern(word):
    pattern = r"(\/\w+\.\w+$)"
    result = re.search(pattern, word)
    return result[0].replace("/", "")

def run():
    filepath = sys.argv
    result = {pattern(key):char_type(key) for key in filepath[1:]}
    if len(result) > 0:
        for key, value in result.items():
            print(f"The encoding for file '{key}' is", value, sep=': ')
    else:
        print('Enter a parameter!')
    
if __name__ == '__main__':
    run()