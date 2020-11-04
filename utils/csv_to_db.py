#!/usr/bin/env python3
import os

import pandas as pd
from sqlalchemy import create_engine

script_path = os.path.dirname(os.path.abspath(__file__))


def upsert_db(data_path=f"{script_path}/../data/cars.csv"):
    df = pd.read_csv(data_path)
    engine = create_engine("postgresql://mpa:maprochaineauto@carstore3000_db_1/carstore3000")
    df.to_sql('cars', engine, index=True, if_exists='replace')


if __name__ == '__main__':
    print("Updating data ...")
    upsert_db()
