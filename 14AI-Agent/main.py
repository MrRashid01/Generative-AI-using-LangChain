import os
import requests
import json

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

load_dotenv()

search_tool = DuckDuckGoSearchRun()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

@tool
def get_weather_data(city:str)->str:
    """
    Get the current weather data for a given city using the Weatherstack API.
    """
    api_key = os.getenv("WEATHERSTACK_API_KEY")
    if not api_key:
        return "Weatherstack API key is not set. Please set the WEATHERSTACK_API_KEY environment variable."
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Error fetching weather data."


# print(search_tool.invoke("what is the capital of Madhya Pradesh ? "))

# print(get_weather_data.invoke({"city": "Bhopal"}))
tools = [
    search_tool,
    get_weather_data
]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a helpful AI assistant.

    You can use web search to find information.
    You can use the weather tool to get current weather.

    When the user asks a question requiring external
    information, use the appropriate tools.

    If one task depends on another, complete the
    first task before performing the next one.

    Give a clear and simple final answer.
    """
)

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is the capital of Japan?"
        }
    ]
})

for message in response["messages"]:
    print("\n-------------------------")
    print("Message Type:", message.type)
    print("Message Content:", message.content)

    if hasattr(message, "tool_calls") and message.tool_calls:
        print("Tool Calls:", message.tool_calls)