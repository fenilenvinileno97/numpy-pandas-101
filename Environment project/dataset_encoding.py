import pandas as pd

def read_csv_with_encoding(filepath, encoding):
    try:
        df = pd.read_csv(filepath, sep=',', header=0, encoding=encoding)
        return df
    except UnicodeDecodeError:
        print(f"Error reading file with {encoding} encoding. Trying next encoding...")

def run():
    file_path = '../../Datasets/CO2_emission_by_countries.csv'
    encodings = ['CP949', 'euc-kr', 'utf-8', 'windows-1252' ]

    for encoding in encodings:
        df = read_csv_with_encoding(file_path, encoding)
        if df is not None:
            print(f"File successfully read with encoding: {encoding}")
            # Perform operations on the DataFrame 'df' as needed
            print(df.head())  # Example: print the first few rows of the DataFrame
            break
    
if __name__ == '__main__':
    run()