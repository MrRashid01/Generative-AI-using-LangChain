from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

loader = DirectoryLoader(
    "my_documents",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

print("Number of documents:", len(documents))

for document in documents:
    print("\n------------------")
    print(document.page_content)
    print(document.metadata)