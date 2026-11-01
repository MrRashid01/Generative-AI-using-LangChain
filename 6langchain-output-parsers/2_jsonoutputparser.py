from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="""
Give information about the following person.

Person: {person}

Return the answer as JSON with these fields:

name
profession
country
""",
    input_variables=["person"]
)

chain = prompt | model | parser

result = chain.invoke({
    "person": "Virat Kohli"
})

print(result)
print(type(result))