from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

prompt = PromptTemplate(
    template="Explain {topic} in 3 simple points.",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "topic": "Binary Search"
})

print(result)