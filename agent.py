from langchain.agents import create_agent
def build_agent(llm,tools,prompt):
    agent=create_agent(
        model=llm,
        tools=tools,
        system_prompt=prompt
    )
    return agent