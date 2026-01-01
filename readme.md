# LangGraph and Django based AI agent

### This project implements a multi-agent AI assistant built using LangChain, LangGraph, Django, and OpenAI models, designed to go beyond a traditional single-agent chatbot architecture.
## At the core of the system is a LangGraph Supervisor node that dynamically routes user queries to the most appropriate agent based on intent. This architecture enables clean separation of responsibilities while maintaining a unified conversational interface.

##### Link for the Demo YouTube video to verify the working of this project-> https://youtu.be/1Csm94pjuUA
________________________________________________________________________________________________________________________________________

## Agent Architecture
The assistant coordinates between two specialized agents:

#### Document Management Agent

- Performs full CRUD operations on a Django-backed database

- Can create documents, assign titles, add or update content, retrieve stored files, and delete them based on natural language instructions

- Uses Django ORM with SQLite as the database (chosen for simplicity and native Django integration)

#### Movie Discovery Agent

- Fetches real-time movie data using GET requests to the TMDB API

- Supports movie search, discovery, and metadata retrieval based on user queries

- The Supervisor node ensures that each request is handled by the correct agent, allowing the system to scale cleanly as more agents are added in the future.

_______________________________________________________________________________________________________________________________________

## Backend & Tooling

- Django serves as the backend, managing APIs, database interactions, and application logic.

- SQLite is used as the database for rapid prototyping and reliability.

- Jupyter Notebooks are integrated for experimenting with, debugging, and testing AI agents in isolation before deploying them into the main system.

_______________________________________________________________________________________________________________________________________

## Note / What Went Wrong

During development, create_react_agent from langgraph.prebuilt was deprecated, forcing a shift away from the original Supervisor-based setup. The fallback option, create_agent from langchain.agents, was not compatible with the LangGraph Supervisor node.
To keep the system working, a lightweight LLM-based smart router was implemented to decide which agent to call. While functional, this approach lacked the structure and robustness of the Supervisor node.
Still, it was a valuable lesson in handling breaking changes in rapidly evolving AI frameworks.

_______________________________________________________________________________________________________________________________________
_______________________________________________________________________________________________________________________________________
