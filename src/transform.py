def transform_data(df):
    """
    Transform manufacturing dataset
    """

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Example KPI calculation
    if "defect_count" in df.columns and "production_volume" in df.columns:
        df["defect_rate"] = df["defect_count"] / df["production_volume"]

    print("Data transformed successfully")

    return df