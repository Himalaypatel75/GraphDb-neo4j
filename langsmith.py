from dotenv import load_dotenv

load_dotenv()
import os

os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')



from langchain_groq import ChatGroq
from langsmith import traceable

# Initialize Groq client (direct initialization)
client = ChatGroq(model="llama3-70b-8192")

@traceable  # Auto-trace this function
def pipeline(user_input: str):
    # Depending on Groq's API, adjust method for creating completions
    result = client.invoke([{"role": "user", "content": user_input}])
    
    # Return the result
    return result

# Test the function
response = pipeline("Hello, world!")
print(response.content)  