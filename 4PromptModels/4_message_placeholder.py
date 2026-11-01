from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.messages import (
    HumanMessage,
    AIMessage
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

history = [
    HumanMessage(
        content="My name is Aryan."
    ),

    AIMessage(
        content="Nice to meet you, Aryan!"
    )
]

messages = prompt.invoke({
    "chat_history": history,
    "query": "What is my name?"
})

print(messages)