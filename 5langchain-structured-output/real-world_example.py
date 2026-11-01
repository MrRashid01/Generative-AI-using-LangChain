from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Literal

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


class ProductReview(BaseModel):

    sentiment: Literal["positive", "negative", "neutral"]

    summary: str = Field(
        description="Short summary of the review"
    )

    pros: list[str] = Field(
        description="Positive points"
    )

    cons: list[str] = Field(
        description="Negative points"
    )


structured_model = model.with_structured_output(ProductReview)


review = """
The Samsung phone has an amazing camera and excellent battery life.
The processor is also very fast.

However, the phone is expensive and quite heavy.
Overall, I really like the phone.
"""

result = structured_model.invoke(review)

print("Sentiment:", result.sentiment)
print("Summary:", result.summary)
print("Pros:", result.pros)
print("Cons:", result.cons)