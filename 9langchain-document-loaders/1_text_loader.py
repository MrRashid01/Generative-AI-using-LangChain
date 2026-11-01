from langchain_community.document_loaders import TextLoader

loader = TextLoader("cricket.txt", encoding="utf-8")

documents = loader.load()

print("Type:", type(documents))

print("\nNumber of documents:", len(documents))

print("\nDocument:")
print(documents[0])

print("\nContent:")
print(documents[0].page_content)

print("\nMetadata:")
print(documents[0].metadata)