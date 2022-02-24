import pandas as pd


def read_file(file):
    df = pd.read_excel(file)
    return df


def extracting_medicine_name(df):
    columns_headlines = df.columns.ravel()
    medicine_name = df[columns_headlines[0]]
    names = pd.DataFrame(medicine_name)

    list_of_names = [str(row[1][0]) for row in names.iterrows()]

    return list_of_names


def get_expiration_date(df):
    columns_headlines = df.columns.ravel()
    expiration_dates = df[columns_headlines[1]]
    dates = pd.DataFrame(expiration_dates)

    list_of_dates = [str(row[1][0]) for row in dates.iterrows()]

    return list_of_dates


def get_quantity(df):
    columns_headlines = df.columns.ravel()
    quantity = df[columns_headlines[2]]
    quantity = pd.DataFrame(quantity)

    list_of_quantity = [row[1][0] for row in quantity.iterrows()]

    return list_of_quantity


def get_minimum_inventory_index(df):
    columns_headlines = df.columns.ravel()
    minimum_inventory = df[columns_headlines[3]]
    inventory = pd.DataFrame(minimum_inventory)

    list_of_inventory = [row[1][0] for row in inventory.iterrows()]

    return list_of_inventory
