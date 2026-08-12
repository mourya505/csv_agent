from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
llm_groq=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
    )
