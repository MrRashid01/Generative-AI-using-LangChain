from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful {role}."
    ),
    (
        "human",
        "{question}"
    )
])

chain = prompt | model

role = input("Enter AI role: ")
question = input("Enter your question: ")

result = chain.invoke({
    "role": role,
    "question": question
})

print("\nAI:", result.content)