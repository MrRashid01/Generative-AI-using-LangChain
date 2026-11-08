from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

llm=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers and return their product.
    """
    return a * b

# result = multiply.invoke({
#     "a":3,
#     "b":3
# })

# print("Total Result: ",result)

llm_with_tools = llm.bind_tools([multiply])

# response = llm_with_tools.invoke(
#     "Can you multiply 3 by 1000?"
# )

# Step 6: Check tool calls
# print("Tool Calls:", response.tool_calls)

# User query
query = HumanMessage(
    content="Can you multiply 3 by 1000?"
)

messages = [query]

# Ask Gemini
ai_message = llm_with_tools.invoke(messages)

messages.append(ai_message)

for tool_call in ai_message.tool_calls:

    if tool_call["name"] == "multiply":
        tool_result = multiply.invoke(tool_call)

        messages.append(tool_result)

final_response =llm_with_tools.invoke(messages)
print("Final Answer: ",final_response.content)
       