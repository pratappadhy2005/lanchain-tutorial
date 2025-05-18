from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

result = llm.invoke("What's the square root of 49?")

print(result.content)
