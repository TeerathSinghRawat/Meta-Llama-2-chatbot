from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
os.environ["LANGCHAIN_TRACING_V2"]="true"

#Prompt Template 

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant . Please respond to queries"),
        ("user","Question:{question}")
    ]

)

# streamlit framework
st.title("Langchain Demo with Meta Llama2")
input_text=st.text_input("Search")

llm=Ollama(model="Llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({"question":input_text}))