import pandas as pd
import tools
from parse import parse_question
from llm import llm
df = pd.read_csv("data.csv")
tools.df=df
print(tools.total_sales.invoke({"quarter": "Q1_Sales"}))