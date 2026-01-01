from langchain_openai import ChatOpenAI
from langgraph_supervisor import create_supervisor
# from langchain.agents import AgentExecutor #Deprecated to idk where
from langgraph.graph import StateGraph

from ai.llms import get_openai_model
from ai import agents

def get_supervisor(model=None, checkpointer=None):
    llm_model=get_openai_model(model=model)
    return create_supervisor(
        [agents.get_document_agent(),agents.get_movie_discovery_agent()],
        model=llm_model,
        prompt=(
            "You are supposed to manage and assign work to a document agent and a movie discovery agent."
        )
    ).compile(checkpointer=checkpointer)


# Trying to create a LangGraph graph to create nodes and pass them to supervisor as it reads nodes and everything else is pretty much cosmetic.
# Moreover, I used the create_agent method here which is an inferior version to create_react_agent method which has been removed from langgraph.prebuilt
# langchain.agents but is not usable from there so I had to go with the create_agent method which does not support multi-agents systems. In order to
# make it compatible with the supervisor agent I'll have to go for graph.
# WISH ME LUCK!!!😭🙏🏻✨


