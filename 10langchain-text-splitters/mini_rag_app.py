from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load PDF
loader = PyPDFLoader("dl-curriculum.pdf")

documents = loader.load()

print("Documents:", len(documents))

# 2. Create splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# 3. Split documents
chunks = splitter.split_documents(documents)

print("Chunks:", len(chunks))

# 4. Print first chunk
print("\nFirst chunk:")
print(chunks[0].page_content)

# 5. Print metadata
print("\nMetadata:")
print(chunks[0].metadata)