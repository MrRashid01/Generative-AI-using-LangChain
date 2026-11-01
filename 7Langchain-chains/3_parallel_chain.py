from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

parser = StrOutputParser()

explanation_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

example_prompt = ChatPromptTemplate.from_template(
    "Give 3 simple examples of {topic}."
)

advantages_prompt = ChatPromptTemplate.from_template(
    "Give 3 advantages of {topic}."
)

explanation_chain = explanation_prompt | model | parser

example_chain = example_prompt | model | parser

advantages_chain = advantages_prompt | model | parser

parallel_chain = RunnableParallel(
    explanation=explanation_chain,
    examples=example_chain,
    advantages=advantages_chain
)

result = parallel_chain.invoke({
    "topic": "Artificial Intelligence"
})

print("EXPLANATION:")
print(result["explanation"])

print("\nEXAMPLES:")
print(result["examples"])

print("\nADVANTAGES:")
print(result["advantages"])