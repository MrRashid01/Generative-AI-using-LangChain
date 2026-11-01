from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_text = """
# Artificial Intelligence

Artificial Intelligence is a field of computer science.

## Machine Learning

Machine Learning allows computers to learn from data.

## Deep Learning

Deep Learning uses neural networks.

### Applications

Deep Learning is used in computer vision and NLP.
"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

documents = splitter.split_text(markdown_text)

for doc in documents:
    print("\n----------------")
    print(doc.page_content)
    print(doc.metadata)