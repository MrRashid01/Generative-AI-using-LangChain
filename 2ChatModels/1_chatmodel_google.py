from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0,
    max_output_tokens=100
)

result = model.invoke(
    "Suggest me 5 Indian meals. Give only the names."
)

print(result.content)

print("Output tokens:", result.usage_metadata)
print("Finish reason:", result.response_metadata.get("finish_reason"))