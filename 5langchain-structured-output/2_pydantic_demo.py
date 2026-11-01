from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


class Review(BaseModel):

    key_themes: list[str] = Field(
        description="Important themes discussed in the review"
    )

    summary: str = Field(
        description="Short summary of the review"
    )

    sentiment: Literal["pos", "neg"] = Field(
        description="Positive or negative sentiment"
    )

    pros: Optional[list[str]] = Field(
        description="Advantages of the product"
    )

    cons: Optional[list[str]] = Field(
        description="Disadvantages of the product"
    )

    name: Optional[str] = Field(
        description="Name of the reviewer"
    )


structured_model = model.with_structured_output(Review)


result = structured_model.invoke("""
I recently bought the Samsung Galaxy S24 Ultra.

The camera is excellent and the processor is extremely fast.
The battery lasts the whole day and the S-Pen is useful.

However, the phone is expensive and quite large.

Review by Aryan.
""")

print(result)
print(type(result))
print(result.name)
print(result.sentiment)
print(result.summary)
print(result.pros)