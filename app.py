import pandas as pd
from tools import *
from parse import parse_question
from llm import llm
df = pd.read_csv("data.csv")
question = input("Ask your question: ")

llm=llm.invoke("hello")
print(llm.content)