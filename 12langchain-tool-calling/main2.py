from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

llm= ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

@tool
def add(a: int, b: int) -> int:
    """Add two numbers and return their sum."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return their product."""
    return a * b

@tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers and return their difference."""
    return a - b

tools = [add, multiply, subtract]

tools_dist={
    tool.name: tool for tool in tools
}

llm_with_tools = llm.bind_tools(
    tools
)

messages =[
    HumanMessage(
        content="Add 10 and 20, multiply the result by 2, then subtract 15."
    )
]

while True:
    ai_message = llm_with_tools.invoke(messages)
    messages.append(ai_message)

    print("\nAI:", ai_message.content)

    if not ai_message.tool_calls:
        print("\nFinal Answer:", ai_message.content)
        break

    for tool_call in ai_message.tool_calls:
        tool_name = tool_call["name"]

        print(f"\nCalling tool: {tool_name} with arguments: {tool_call['args']}")

        select_tool = tools_dist[tool_name]

        tool_result = select_tool.invoke(tool_call)

        print(f"\nTool Result: " ,tool_result.content)

        messages.append(tool_result)