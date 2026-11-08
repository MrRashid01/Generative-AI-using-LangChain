# from langchain_core.tools import tool

# @tool
# def multiply(a: int, b: int) -> int:
#     """Multiply two numbers."""
#     return a * b

# result = multiply.invoke({
#     "a": 3,
#     "b": 5
# })

# print(result)
# print(multiply.name)
# print(multiply.description)
# print(multiply.args)

# from langchain_core.tools import StructuredTool
# from pydantic import BaseModel, Field

# class MultiplyInput(BaseModel):

#     a: int = Field(
#         ...,
#         description="The first number"
#     )

#     b: int = Field(
#         ...,
#         description="The second number"
#     )


# def multiply_func(a: int, b: int) -> int:
#     return a * b


# multiply_tool = StructuredTool.from_function(
#     func=multiply_func,
#     name="multiply",
#     description="Multiply two numbers",
#     args_schema=MultiplyInput
# )
# result = multiply_tool.invoke({
#     "a": 3,
#     "b": 3
# })

# print(result)

from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class MultiplyInput(BaseModel):

    a: int = Field(..., description="First number")

    b: int = Field(..., description="Second number")


class MultiplyTool(BaseTool):

    name: str = "multiply"

    description: str = "Multiply two numbers"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b

multiply_tool = MultiplyTool()

result = multiply_tool.invoke({
    "a": 3,
    "b": 3
})

print(result)