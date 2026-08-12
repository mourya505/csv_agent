import pandas as pd
from tools import (
    total_sales,
    average_sales,
    highest_sales_region,
    highest_sales_product,
    shape_of_table,
    column_name,
    unique_column,
    sales_growth,
    regional_sales_data,
    abs_change
)
import tools
from parse import parse_question
from llm import llm_groq
from agent import build_agent
from rich import print

df = pd.read_csv("data.csv")
tools.df=df
tool_list = [
    total_sales,
    average_sales,
    highest_sales_region,
    highest_sales_product,
    shape_of_table,
    column_name,
    unique_column,
    sales_growth,
    regional_sales_data,
    abs_change

]

llm=llm_groq
prompt="""You are an AI Data Analyst.

You answer questions about the sales dataset by using the available tools.

Rules:
1. Always use a tool when the question requires data from the dataset.
2. Never invent numbers.
3. Select the appropriate tool based on the user's question.
4. Use the correct quarter.
5. Explain the result clearly to the user.
6. If the query can be answered in one word then dont try to explain
7. Never try to explain whole calculation without user asking for it
 """
agent = build_agent(
    llm=llm,
    tools=tool_list,
    prompt=prompt
)
print("ask your question and type exit to quit")
while(True):
    question=input("you:")
    if question.lower()=="exit":
        break
    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })
    print(response["messages"][-1].content)