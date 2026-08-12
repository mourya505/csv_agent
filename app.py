import pandas as pd
from analyzer import *

df = pd.read_csv("data.csv")

print(total_sales(df, "Q1_Sales"))

print(average_sales(df, "Q2_Sales"))

print(highest_sales_region(df, "Q3_Sales"))

print(highest_sales_product(df, "Q4_Sales"))