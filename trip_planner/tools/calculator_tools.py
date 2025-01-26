from langchain.tools import tool


class CalculatorTools:

    @tool("Make a calculation")
    def calculate(operation):
        """
        Useful to perform any mathematical calculations like addition, subtraction, multiplication, division, etc.
        The input to this tool should be a mathematical expression.
        Some examples are `200*7` or `5000/2*10`
        """

        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"


# ################################################################################
# # For a more stricter calculation, you can use the one below:

# from pydantic import BaseModel, Field
# from langchain.tools import tool


# # Define a pydantic model for the tool's input parameters
# class CalculationInput(BaseModel):
#     operation: str = Field(..., description="The mathematical operation to perform")
#     factor: float = Field(
#         ..., description="A factor by which to multply the result of the operation"
#     )


# # Use the tool decorator with
# @tool("perform calculation", args_schema=CalculationInput, return_direct=True)
# def perform_calculation(operation: str, factor: float) -> str:
#     """
#     Perform a specified mathematical operation and multiplies the result by a given factor.

#     Parameters:
#     - operation (str): A string representing a mathematical operation (e.g., "10 + 5")
#     - factor (float): A factor by which to multiply the result of the operation.

#     Returns:
#     - A string representation of hte calculation result.
#     """
#     # Perform the calculation
#     result = eval(operation) * factor

#     # Return the result as a string
#     return f"The result of '{operation}' multiplied by {factor} is {result}"
