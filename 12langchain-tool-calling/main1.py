
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

# --------------------------------
# STEP 1: Initialize Gemini
# --------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# --------------------------------
# STEP 2: Create Custom Tools
# --------------------------------

@tool
def add(a: int, b: int) -> int:
    """Add two numbers and return their sum."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return their product."""
    return a * b


# --------------------------------
# STEP 3: Bind Both Tools
# --------------------------------

llm_with_tools = llm.bind_tools(
    [add, multiply]
)


# --------------------------------
# STEP 4: User Query
# --------------------------------

query = HumanMessage(
    content="First add 5 and 5, then multiply the result by 5."
)

messages = [query]


# --------------------------------
# STEP 5: Call ADD Tool
# --------------------------------

# Bind only add for this stage
add_llm = llm.bind_tools(
    [add],
    tool_choice="any"
)

print("\nCalling Gemini for Addition...")

ai_message = add_llm.invoke([
    HumanMessage(
        content="Call the add tool with a=5 and b=5."
    )
])

print("Gemini Tool Calls:", ai_message.tool_calls)

if not ai_message.tool_calls:
    raise RuntimeError("Gemini did not request the add tool.")

# Execute add tool
addition_result = add.invoke(
    ai_message.tool_calls[0]
)

print("Addition Result:", addition_result.content)


# --------------------------------
# STEP 6: Call MULTIPLY Tool
# --------------------------------

# Bind only multiply for this stage
multiply_llm = llm.bind_tools(
    [multiply],
    tool_choice="any"
)

print("\nCalling Gemini for Multiplication...")

ai_message2 = multiply_llm.invoke([
    HumanMessage(
        content=(
            f"The addition result is {addition_result.content}. "
            f"Now call the multiply tool with "
            f"a={addition_result.content} and b=5."
        )
    )
])

print("Gemini Tool Calls:", ai_message2.tool_calls)

if not ai_message2.tool_calls:
    raise RuntimeError("Gemini did not request the multiply tool.")

# Execute multiply tool
multiply_result = multiply.invoke(
    ai_message2.tool_calls[0]
)

print("Multiplication Result:", multiply_result.content)


# --------------------------------
# STEP 7: Generate Final Response
# --------------------------------

final_response = llm.invoke(
    f"""
    The user asked: First add 5 and 5,
    then multiply the result by 5.

    Addition result: {addition_result.content}
    Multiplication result: {multiply_result.content}

    Explain the final answer in one sentence.
    """
)

print("\nFinal Answer:", final_response.content)
