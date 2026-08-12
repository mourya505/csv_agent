import pandas as pd
from langchain_core.tools import tool
df=None

@tool
def total_sales(quarter:str):
    """calculates total sales for given data frame and quarter"""
    return df[quarter].sum()

@tool
def average_sales(quarter:str):
    """claculates average sales for given data frame and quarter"""
    return df[quarter].mean()


def highest_sales_region(quarter:str):
    """calculates highest sales fo a region using the provdied quarter"""
    result = (
        df.groupby("Region")[quarter]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_dict()


def highest_sales_product(quarter:str):
    """calculates highest sales of a product sing provided data frame and quarter"""

    result = (
        df.groupby("Product")[quarter]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_dict()