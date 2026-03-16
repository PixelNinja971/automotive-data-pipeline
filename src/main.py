from extract import extract_data
from transform import transform_data
from load import load_data

FILE_PATH = "data/manufacturing_defect_dataset.csv"

def run_pipeline():

    df = extract_data(FILE_PATH)

    df_transformed = transform_data(df)

    load_data(df_transformed)

if __name__ == "__main__":
    run_pipeline()