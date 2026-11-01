from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("Social_Network_Ads.csv")

documents = loader.load()

print("Number of documents:", len(documents))

print("\nFirst document:")
print(documents[0])

print("\nContent:")
print(documents[0].page_content)

print("\nMetadata:")
print(documents[0].metadata)