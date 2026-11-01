from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    "https://leetcode.com/problems/find-x-value-of-array-i/description/?envType=daily-question&envId=2026-09-21"
)

documents = loader.load()

print("Number of documents:", len(documents))

print("\nContent:")
print(documents[0].page_content)

print("\nMetadata:")
print(documents[0].metadata)