import pandas as pd
from langchain_core.tools import tool
df=None

@tool
def total_sales(quarter:str):
    """calculates total sales for given data frame and quarter
     The quarter must be one of:
    Q1_Sales, Q2_Sales, Q3_Sales, Q4_Sales.
    """
    return df[quarter].sum()

@tool
def average_sales(quarter:str):
    """claculates average sales for given data frame and quarter
     The quarter must be one of:
    Q1_Sales, Q2_Sales, Q3_Sales, Q4_Sales.
    """
    return df[quarter].mean()

@tool
def highest_sales_region(quarter:str):
    """calculates highest sales fo a region using the provdied quarter
     The quarter must be one of:
    Q1_Sales, Q2_Sales, Q3_Sales, Q4_Sales.
    """
    result = (
        df.groupby("Region")[quarter]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_dict()

@tool
def highest_sales_product(quarter:str):
    """calculates highest sales of a product sing provided data frame and quarter
     The quarter must be one of:
    Q1_Sales, Q2_Sales, Q3_Sales, Q4_Sales.
    """

    result = (
        df.groupby("Product")[quarter]
        .sum()
        .sort_values(ascending=False)
    )

    return result.to_dict()
@tool
def shape_of_table():
    """returns number of rows and columns of the data"""
    row=df.shape[0]
    column=df.shape[1]
    return row,column
@tool
def column_name():
    """returns the column names"""
    return df.columns
@tool
def unique_column(column_name:str):
    """returns unique elemnts in the column"""
    if column_name not in df.columns:
        return f"Column {column_name} does not exist. Available columns are: Region, Product, Q1_Sales, Q2_Sales, Q3_Sales, Q4_Sales."

    return df[column_name].unique().tolist()
@tool
def sales_growth(start:str,end:str):
    """use this when ever claculating growth percentage
    Q1 or q1 must be Q1_sales
    Q2 or q2 must be Q2_sales
    Q3 or q3 must be Q3_sales
    Q4 or q4 must be Q4_sales
    """
    start_sales=total_sales.invoke(start)
    if start_sales==0:
        return
    end_sales=total_sales.invoke(end)
    result=((end_sales-start_sales)/start_sales)*100
    return result
@tool
def regional_sales_data(start:str,end:str):
     """to return sales data of each regions for given quarters
        Q1 or q1 must be Q1_sales
        Q2 or q2 must be Q2_sales
        Q3 or q3 must be Q3_sales
        Q4 or q4 must be Q4_sales
        """
     result1=df.groupby("Region")[start].sum()
     result2=df.groupby("Region")[end].sum()
     com=pd.concat([result1,result2],axis=1)
     return com
@tool
def abs_change(start:str,end:str):
    """use this to find absolute change"""
    return df[end]-df[start]