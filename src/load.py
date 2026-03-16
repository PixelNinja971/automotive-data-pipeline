import pandas as pd
from sqlalchemy import create_engine
import time

def load_data(df):

    # attendre que postgres démarre
    time.sleep(10)

    engine = create_engine(
        "postgresql://postgres:postgres@postgres:5432/production_db"
    )

    df.to_sql(
        "manufacturing_production",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into PostgreSQL")