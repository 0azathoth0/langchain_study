from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.agents.middleware import (SummarizationMiddleware,HumanInTheLoopMiddleware,
                                         PIIMiddleware,TodoListMiddleware,AgentMiddleware)
from langchain.agents.middleware import hook_config, ModelRequest, ModelResponse, wrap_model_call, wrap_tool_call
from langchain.agents.middleware import before_model, after_model
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
from rich import print as rprint
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.tools import tool
from langgraph.runtime import Runtime
from typing import Any, Callable
from loguru import logger
from langchain.agents import AgentState