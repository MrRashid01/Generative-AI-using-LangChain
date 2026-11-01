from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Artificial Intelligence is a field of computer science.
It focuses on creating machines that can perform tasks
that normally require human intelligence.

Machine Learning is a subset of Artificial Intelligence.
It allows computers to learn patterns from data.

Deep Learning is a subset of Machine Learning.
It uses neural networks with many layers.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)