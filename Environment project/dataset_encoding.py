#!/usr/bin/env python3

import pandas as pd
import sys
from encoded import encodings

def read_csv_with_encoding(filepath, encoding):
    try:
        df = pd.read_csv(filepath, sep=',', header=0, encoding=encoding)
        return df
    except UnicodeDecodeError:
        print(f"Error reading file with {encoding} encoding. Trying next encoding...")

def run():
    file_path = '../../Datasets/cars/cars.csv'
    encodings_list = encodings

    for encoding in encodings_list:
        df = read_csv_with_encoding(file_path, encoding)
        if df is not None:
            print(f"File successfully read with encoding: {encoding}")
            # Perform operations on the DataFrame 'df' as needed
            print(df.head())  # Example: print the first few rows of the DataFrame
        if df is None:
            print("Find out other appropiate encodings")
            break
    
if __name__ == '__main__':
    run()