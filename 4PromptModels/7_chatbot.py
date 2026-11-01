from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        "You are a helpful AI assistant."
    ),

    MessagesPlaceholder(
        variable_name="chat_history"
    ),

    (
        "human",
        "{query}"
    )
])

chain = prompt | model

chat_history = []

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    result = chain.invoke({
        "chat_history": chat_history,
        "query": query
    })

    print("AI:", result.content)

    chat_history.append(
        HumanMessage(content=query)
    )

    chat_history.append(
        AIMessage(content=result.content)
    )