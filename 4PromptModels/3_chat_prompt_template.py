# from langchain_core.prompts import ChatPromptTemplate

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful {role}."),
#     ("human", "Explain {topic} in simple words.")
# ])

# messages = prompt.invoke({
#     "role": "teacher",
#     "topic": "Python"
# })

# print(messages)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {role}."),
    ("human", "Explain {topic} in simple words.")
])

chain = prompt | model

result = chain.invoke({
    "role": "teacher",
    "topic": "Python"
})

print(result.content)