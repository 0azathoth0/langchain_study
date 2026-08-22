import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.utils.function_calling import convert_to_openai_tool
from langchain_core.messages import HumanMessage,SystemMessage
from typing import Optional,Literal
from datetime import datetime
from langchain_core.tools import tool
from pydantic import BaseModel, Field