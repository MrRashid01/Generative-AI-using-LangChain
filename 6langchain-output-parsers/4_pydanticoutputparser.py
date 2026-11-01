from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


class Person(BaseModel):

    name: str = Field(
        description="Name of the person"
    )

    profession: str = Field(
        description="Profession of the person"
    )

    country: str = Field(
        description="Country of the person"
    )


parser = PydanticOutputParser(
    pydantic_object=Person
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