from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dl-curriculum.pdf")

documents = loader.load()

print("Number of documents:", len(documents))

print("\nFirst document:")
print(documents[0])

print("\nFirst page content:")
print(documents[0].page_content)

print("\nMetadata:")
print(documents[0].metadata)