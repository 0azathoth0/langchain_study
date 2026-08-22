import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from typing import Optional,List,TypedDict, Annotated
from enum import Enum
from pydantic import BaseModel, Field,ValidationError
from rich import print as rprint
from dataclasses import dataclass
from pydantic import SecretStr
from langchain_deepseek import ChatDeepSeek