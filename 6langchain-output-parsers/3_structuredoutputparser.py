from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    StructuredOutputParser,
    ResponseSchema
)
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

response_schemas = [
    ResponseSchema(
        name="name",
        description="Name of the person"
    ),

    ResponseSchema(
        name="profession",
        description="Profession of the person"
    ),

    ResponseSchema(
        name="country",
        description="Country of the person"
    )
]

parser = StructuredOutputParser.from_response_schemas(
    response_schemas
)

prompt = PromptTemplate(
    template="""
Give information about {person}.

{format_instructions}
""",
    input_variables=["person"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = prompt | model | parser

result = chain.invoke({
    "person": "Virat Kohli"
})

print(result)
print(type(result))