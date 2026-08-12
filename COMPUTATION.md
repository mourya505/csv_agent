# How Numbers Are Computed

## Overview

The AI Data Analyst uses Python and Pandas to perform numerical
calculations on the uploaded dataset.

The LLM is responsible for understanding the user's question and
selecting the appropriate tool. It does not directly calculate
numerical results from memory.

## Computation Flow

User Question
↓
LangChain Agent
↓
Tool Selection
↓
Python / Pandas Calculation
↓
Computed Result
↓
LLM Explanation
↓
Final Answer

## Examples

### Total Sales

For a selected numerical column:

Total = sum of all values in the column

The calculation is performed using Pandas.

### Average

Average = sum of values / number of values

The calculation is performed using Pandas.

### Percentage Growth

Growth % = ((End Value - Start Value) / Start Value) × 100

Example:

Q1 = 225000
Q2 = 295000

Growth % = ((295000 - 225000) / 225000) × 100
          = 31.11%

### Absolute Change

Absolute Change = End Value - Start Value

Example:

Q1 = 225000
Q2 = 295000

Absolute Change = 295000 - 225000
                = 70000

## Preventing Hallucinations

The agent follows these principles:

1. Numerical questions should be answered using the available
   analytical tools.
2. Calculations are performed by Python/Pandas.
3. The LLM receives the computed result from the tool.
4. The LLM is responsible for explaining the result.
5. The agent should not invent numerical values when the required
   data is unavailable.

## Important Edge Cases

### Division by Zero

If the starting value is zero, percentage growth cannot be
calculated using the standard formula.

The tool should return an appropriate message instead of
performing a division by zero.

### Negative Growth

A negative growth percentage represents a decrease.

Example:

Start = 100
End = 80

Growth = -20%

This should be explained as a 20% decrease.

## Why This Approach?

Separating computation from language generation makes the system
more reliable.

Python/Pandas performs deterministic calculations, while the LLM
handles natural-language understanding, tool selection, and
explanation.