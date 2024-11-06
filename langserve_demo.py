from fastapi import FastAPI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

model = ChatGroq(model="llama3-70b-8192")
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
from langserve import add_routes

add_routes(
    app,
    prompt | model,
    path="/joke",
)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)