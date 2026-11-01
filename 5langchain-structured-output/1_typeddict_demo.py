from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


class Review(TypedDict):

    key_themes: Annotated[
        list[str],
        "List the important themes discussed in the review"
    ]

    summary: Annotated[
        str,
        "Give a short summary of the review"
    ]

    sentiment: Annotated[
        Literal["pos", "neg"],
        "Return positive or negative sentiment"
    ]

    pros: Annotated[
        Optional[list[str]],
        "List the advantages"
    ]

    cons: Annotated[
        Optional[list[str]],
        "List the disadvantages"
    ]

    name: Annotated[
        Optional[str],
        "Name of the reviewer"
    ]


structured_model = model.with_structured_output(Review)


review = """
I recently bought the Samsung Galaxy S24 Ultra.

The phone has an excellent camera and the processor
is extremely fast. The battery also lasts the whole day.

The S-Pen is useful for taking notes.

However, the phone is very expensive and its large size
makes one-handed use uncomfortable.

Review by Aryan.
"""

result = structured_model.invoke(review)

print(result)

print(result["name"])
print(result["summary"])
print(result["sentiment"])
print(result["pros"])
print(result["cons"])