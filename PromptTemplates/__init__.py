from langchain_core.prompts import ChatPromptTemplate
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import MessagesPlaceholder
from .templates import PromptLibrary