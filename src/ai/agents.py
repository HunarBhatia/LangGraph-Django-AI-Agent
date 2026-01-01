from langchain.agents import create_agent

from ai.llms import get_openai_model
from ai.tools import(
    document_tools,
    movie_discovery_tools,
)
def get_document_agent(checkpointer=None):
    model=get_openai_model()

    agent=create_agent(
        model=model,
        tools=document_tools,
        system_prompt="You are a helpful assistant who performs crud operations and calls appropriate tools as and when required.",
        checkpointer=checkpointer,
    )
    return agent

def get_movie_discovery_agent(checkpointer=None):
    model=get_openai_model()

    agent=create_agent(
        model=model,
        tools=movie_discovery_tools,
        system_prompt="You are a helpful agent in finding and discovering information about movies.",
        checkpointer=checkpointer,
    )
    return agent