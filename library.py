
from langchain_openai import AzureOpenAI
from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
#from langchain_community.chat_models import AzureChatOpenAI

from langchain_community.utilities import SQLDatabase
import pymssql
from dotenv import load_dotenv

import os
load_dotenv()

def get_gpt4_model():

    azure_llm = AzureChatOpenAI(
    model="gpt-4",
    deployment_name="ib-chatgpt4-model",
    api_key="cb8bc4e498274c2295903f3a39f58a45",
    azure_endpoint="https://aoi-imperialbrand.openai.azure.com/",
    api_version="2024-02-01", 
    temperature=0.0,)
    return azure_llm

def get_gpt4_turbo_model():
    azure_llm = AzureChatOpenAI(
    model="gpt-4",
    deployment_name="ib-gpt4-turbo",
    api_key="cd76d3802fd642e7895a27ef100daf64",
    azure_endpoint="https://imperial-open-ai-eu.openai.azure.com/",
    api_version="2024-02-15-preview", 
    temperature=0.0,)
    return azure_llm

def get_embedding_model():
    azure_embed_model = AzureOpenAIEmbeddings(
    model="text-embedding-ada-002",
    azure_deployment="text-embedding-ada-002",
    api_key="cb8bc4e498274c2295903f3a39f58a45",
    azure_endpoint="https://aoi-imperialbrand.openai.azure.com/",
    )
    return azure_embed_model

def connect_to_database():
    server = "ib-azure-sql.database.windows.net"
    database = "ImperialBrands_norm"
    username = "sqladmin"
    password = "Admin#123"

    connection_string = f"mssql+pymssql://{username}:{password}@{server}/{database}"
    db_connection = SQLDatabase.from_uri(connection_string)

    return db_connection