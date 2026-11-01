from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

response = model.invoke("Say hello in one sentence")

print(response.content)