from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

prompt = PromptTemplate(
    template="""
Create a prompt for an AI that helps a student
learn {topic}.

The prompt should:
1. Explain the concept simply.
2. Give an example.
3. Ask one practice question.
""",
    input_variables=["topic"]
)

chain = prompt | model

result = chain.invoke({
    "topic": "Binary Search"
})

print(result.content)