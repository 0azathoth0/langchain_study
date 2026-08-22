import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from rich import print as rprint
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langchain_core.messages import RemoveMessage
from typing import Any
from langgraph.runtime import Runtime
from langchain.agents import AgentState
from langchain.agents.middleware import before_model, after_model
from langgraph.store.postgres import PostgresStore
from langchain.embeddings import init_embeddings
from langgraph.store.memory import InMemoryStore
from pprint import pprint
from typing import Required, NotRequired
from langchain.tools import tool, ToolRuntime
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain_core.messages import BaseMessage
from langchain.agents.structured_output import ToolStrategy
from pydantic import BaseModel, Field