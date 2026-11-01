from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

parser = StrOutputParser()

math_prompt = ChatPromptTemplate.from_template(
    """
You are a math teacher.

Solve this problem step by step:

{question}
"""
)

general_prompt = ChatPromptTemplate.from_template(
    """
You are a helpful teacher.

Answer this question in simple words in 2 sentences: 

{question}
"""
)

math_chain = math_prompt | model | parser

general_chain = general_prompt | model | parser


conditional_chain = RunnableBranch(
    (
        lambda x: "math" in x["question"].lower()
        or any(char.isdigit() for char in x["question"]),
        math_chain
    ),
    general_chain
)


result = conditional_chain.invoke({
    "question": "What is 25 + 30?"
})

print(result)