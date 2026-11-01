from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Step 1
prompt1 = PromptTemplate(
    template="Explain {topic} in simple words.",
    input_variables=["topic"]
)

# Step 2
prompt2 = PromptTemplate(
    template="Summarize the following explanation in 2 lines:\n\n{explanation}",
    input_variables=["explanation"]
)

parser = StrOutputParser()

chain = (
    prompt1
    | model
    | parser
    | prompt2
    | model
    | parser
)

explanation = chain.invoke({
    "topic": "Artificial Intelligence"
})

print("summary : ", explanation)