from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

prompt = PromptTemplate(
    template="Explain {topic} in simple words.",
    input_variables=["topic"]
)

chain = prompt | model

result = chain.invoke({
    "topic": "Machine Learning"
})

print(result.content)