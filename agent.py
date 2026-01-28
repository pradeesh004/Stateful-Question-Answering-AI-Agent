from google.adk.agents import Agent

root_agent = Agent(
    name="agent_1",
    model="gemini-2.5-flash-lite",
    description="Question-answering-agent",
    instruction="""
    your are an intelligent agent. you need to answer the user's question based  on the histroy that you will get.
    user_name:
    {user_name}
    user_content:
    {user_content}.
    """
)