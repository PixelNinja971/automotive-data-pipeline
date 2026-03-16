import pandas as pd 

def extract_data(file_path):

    df = pd.read_csv(file_path)
    print("Data extracted successfully")
    print(df.head())

    return df