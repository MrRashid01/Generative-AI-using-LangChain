from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import Language

code = """
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap=20
)

chunks = splitter.split_text(code)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)
