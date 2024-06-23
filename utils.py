import library as lib

azure_openai_api_key = "cb8bc4e498274c2295903f3a39f58a45"

from langchain.chains import create_sql_query_chain
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.memory import ChatMessageHistory
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from prompts import final_prompt, answer_prompt
import streamlit as st

def get_chain():
    print("Creating chain")

    llm= lib.get_gpt4_turbo_model()
    db= lib.connect_to_database()
    
    generate_query = create_sql_query_chain(llm, db, final_prompt) 
    execute_query = QuerySQLDataBaseTool(db=db)
    rephrase_answer = answer_prompt | llm | StrOutputParser()
    chain = (
    RunnablePassthrough.assign(query=generate_query).assign(
        result=itemgetter("query") | execute_query
    )
    | rephrase_answer
)

    return chain

def create_history(messages):
    history = ChatMessageHistory()
    for message in messages:
        if message["role"] == "user":
            history.add_user_message(message["content"])
        else:
            history.add_ai_message(message["content"])
    return history

def invoke_chain(question,messages):
    chain = get_chain()
    history = create_history(messages)
    response = chain.invoke({"question": question, "messages":history.messages})
    history.add_user_message(question)
    history.add_ai_message(response)
    return response



