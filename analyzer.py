import pandas as pd

def total_sales(df, quarter):
    return df[quarter].sum()


def average_sales(df, quarter):
    return df[quarter].mean()


def highest_sales_region(df, quarter):

    result = (
        df.groupby("Region")[quarter]
        .sum()
        .sort_values(ascending=False)
    )

    return result


def highest_sales_product(df, quarter):

    result = (
        df.groupby("Product")[quarter]
        .sum()
        .sort_values(ascending=False)
    )

    return result