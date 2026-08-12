# AI CSV / Data Q&A Agent

An AI-powered data analysis agent that allows users to ask
natural-language questions about CSV datasets.

The agent uses LangChain for agent orchestration, Groq as the LLM,
and Pandas for deterministic data analysis and calculations.

---

## Problem

Analyzing CSV data often requires knowledge of Python, Pandas, SQL,
or spreadsheet formulas.

This project allows users to ask questions about their dataset
using plain English.

For example:

- How many rows and columns are in the dataset?
- What is the total Q1 sales?
- Which region had the highest sales?
- Which region grew fastest?
- What was the absolute increase from Q1 to Q2?

---

## Features

- Load and analyze CSV datasets
- Understand dataset structure
- Identify columns and unique values
- Calculate totals and averages
- Analyze regional and product-level data
- Calculate percentage growth
- Calculate absolute change
- Answer multi-step analytical questions
- Use LangChain agent tool calling
- Use Pandas for data computation
- Generate natural-language explanations

---

## Architecture

```text
                User Question
                     |
                     v
              LangChain Agent
                     |
                     v
              Tool Selection
                     |
        +------------+-------------+
        |            |             |
        v            v             v
     Pandas       Dataset       Analysis
     Tools       Inspection      Tools
        |            |             |
        +------------+-------------+
                     |
                     v
              Computed Result
                     |
                     v
                 Groq LLM
                     |
                     v
             Natural Language
                  Answer