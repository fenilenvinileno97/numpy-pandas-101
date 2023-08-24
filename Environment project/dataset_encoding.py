#!/usr/bin/env python3

import pandas as pd
from char_detection import char_type
from encoded import encodings

def reading_dataframe(filepath, encoding):
    df = pd.read_csv(filepath, sep=',', header=0, encoding=encoding)
    return df.iloc[:5, :5]

def try_reading_with_alternative_encodings(filepath):
    for encoding in encodings:
        try:
            df = reading_dataframe(filepath, encoding)
            return (df, encoding)
        except UnicodeDecodeError:
            pass
    return None

def run():
    file_path = '../../Datasets/CO2_emission_by_countries.csv'
    print(try_reading_with_alternative_encodings(file_path))
    
if __name__ == '__main__':
    run()