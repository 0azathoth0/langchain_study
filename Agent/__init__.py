import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_core.tools import tool
from rich import print as rprint
from typing import Literal,Union
from pydantic import BaseModel, Field
from langchain.agents.structured_output import (ToolStrategy,ProviderStrategy,
                                                StructuredOutputValidationError,
                                                MultipleStructuredOutputsError)