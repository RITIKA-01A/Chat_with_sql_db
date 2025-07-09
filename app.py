import streamlit as st
from pathlib import Path

#Creates an LLM agent that understands SQL
from langchain.agents import create_sql_agent

#Wraps a SQL DB to work with LangChain
from langchain.sql_database import SQLDatabase

#	Defines how the agent behaves (e.g., tool use, reasoning)
from langchain.agents.agent_types import AgentType

#Shows step-by-step agent progress in Streamlit
from langchain.callbacks import StreamlitCallbackHandler

#Provides tools for the SQL agent (e.g., query, schema)
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

#Connects to DB using SQLAlchemy (used by LangChain)
from sqlalchemy import create_engine

#	Native Python interface to SQLite (manual use)
import sqlite3

from langchain_groq import ChatGroq

st.set_page_config(page_title="Langchain:Chat with SQL DB",page_icon="")
st.title(" Langchain: Chat with SQL DB")

INJECTION_WARNING="""
SQL agent can be vulnerable to prompt injection.Use a DB role with limited permission"""


LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"

radio_opt=["Use SQLlite 3 Database-Student.db","Connect to MYSQL Database"]

selected_opt=st.sidebar.radio(label="Choose the DB which you want to chat",options=radio_opt)

if radio_opt.index(selected_opt)==1:
    db_uri=MYSQL
    mysql_host=st.sidebar.text_input("Provide MYSQL Host ")
    mysql_user=st.sidebar.text_input("MYSQL User")
    mysql_password=st.sidebar.text_input("MYSQL Password",type="password")
    mysql_db=st.sidebar.text_input("MYSQL database")

else:
    db_uri=LOCALDB

api_key=st.sidebar.text_input("Enter the Groq api key",type"password")

if not db_uri:
    st.info("Please enter the database information and uri")

if not api_key:
    st.info("Please add the Groq api key")


## LLm model
llm = ChatGroq(grqo_api_key=api_key,model_name="Llama3-8b-8192")

@st.cache_resource(ttl="2h")
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_db=None):
    if db_uri==LOCALDB:
        dbfilepath=(Path(__file__).parent/"students.db").absolute()
        print(dbfilepath)
        creator=lambda: sqlite3.connect(f"file:{dbfilepath}?model=ro",uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    
    elif db_uri==MYSQL:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all the MYSQL Connection details")
            st.stop()
        
        else:
            return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

if db_uri==MYSQL:
    db=configure_db(db_uri,mysql_host,mysql_user,mysql_password,mysql_db)
else:
    db=configure_db(db_uri)


