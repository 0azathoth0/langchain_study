import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage,BaseMessage
from rich import print as rprint