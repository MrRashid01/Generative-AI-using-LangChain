import os
import requests

from dotenv import load_dotenv
from typing import Annotated

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


@tool
def get_conversion_factor(
    base_currency: str,
    target_currency: str
) -> float:
    """
    Fetch the exchange rate between two currencies.
    """

    api_key = os.getenv("EXCHANGE_RATE_API_KEY")

    if not api_key:
        raise ValueError("ExchangeRate API key missing")

    url = (
        f"https://v6.exchangerate-api.com/v6/"
        f"{api_key}/pair/{base_currency.upper()}/"
        f"{target_currency.upper()}"
    )

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()

    if data.get("result") != "success":
        raise ValueError(data.get("error-type", "API error"))

    return float(data["conversion_rate"])


@tool
def convert(
    base_currency_value: float,
    conversion_rate: Annotated[float, InjectedToolArg]
) -> float:
    """
    Convert currency using the given exchange rate.
    """

    return base_currency_value * conversion_rate


llm_with_tools = llm.bind_tools([
    get_conversion_factor,
    convert
])


user_query = "Convert 100 USD into INR."

messages = [
    HumanMessage(content=user_query)
]

print("\nFetching conversion rate...")

rate_llm = llm.bind_tools([get_conversion_factor])

rate_ai_message = rate_llm.invoke([
    HumanMessage(
        content=(
            f"{user_query} "
            "First call get_conversion_factor with "
            "the correct base and target currencies."
        )
    )
])

print("Gemini Tool Calls:", rate_ai_message.tool_calls)

if not rate_ai_message.tool_calls:
    raise RuntimeError("Gemini did not request the rate tool.")

rate_call = rate_ai_message.tool_calls[0]

if rate_call["name"] != "get_conversion_factor":
    raise RuntimeError("Unexpected tool requested.")

# Execute Tool 1
rate_tool_message = get_conversion_factor.invoke(rate_call)

conversion_rate = float(rate_tool_message.content)

print("Conversion Rate:", conversion_rate)

print("\nCalculating converted amount...")

convert_llm = llm.bind_tools([convert])

convert_ai_message = convert_llm.invoke([
    HumanMessage(
        content=(
            f"{user_query} "
            f"The conversion rate is {conversion_rate}. "
            "Call the convert tool with the original amount "
            "from the user's request."
        )
    )
])

print("Gemini Tool Calls:", convert_ai_message.tool_calls)

if not convert_ai_message.tool_calls:
    raise RuntimeError("Gemini did not request the convert tool.")

convert_call = convert_ai_message.tool_calls[0]

if convert_call["name"] != "convert":
    raise RuntimeError("Unexpected tool requested.")

# Inject conversion rate manually
convert_call["args"]["conversion_rate"] = conversion_rate

# Execute Tool 2
convert_tool_message = convert.invoke(convert_call)

converted_amount = float(convert_tool_message.content)

print("Converted Amount:", converted_amount)


final_response = llm.invoke(
    f"""
    The user asked: {user_query}

    Exchange rate: {conversion_rate}
    Converted amount: {converted_amount}

    Give a clear final answer with both currencies
    and the exchange rate.
    """
)

print("\nFinal Answer:")
print(final_response.content)
