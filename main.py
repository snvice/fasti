from fastapi import FastAPI
from typing import Optional
import pandas as pd

app = FastAPI()

df = pd.read_csv('data/FuelConsumption.csv')
columns = df.columns
cars = df.to_dict(orient='records')


@app.get("/data")
async def read_all_data():
    return cars


@app.get("/data/{cylinders}")
async def read_make(cylinders: int):
    # filter_df = df[df.get('MAKE') == make]
    filter_df = df[df['CYLINDERS'] == cylinders]
    filter_df = filter_df.to_dict(orient='records')
    return filter_df


@app.get("/filter")
async def read_data(make: Optional[str] = None, model: Optional[str] = None):
    # Start with the original DataFrame
    filter_df = df

    # Apply filter for 'MAKE' if provided
    if make is not None:
        filter_df = filter_df[filter_df['MAKE'].str.casefold() == make.casefold()]

    # Apply filter for 'MODEL' if provided
    if model is not None:
        filter_df = filter_df[filter_df['MODEL'].str.casefold() == model.casefold()]

    # Convert the filtered DataFrame to a list of dictionaries
    filter_df = filter_df.to_dict(orient='records')
    return filter_df
