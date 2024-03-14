from pandasai.llm import OpenAI 
import os
import streamlit as st
import pandas as pd
from pandasai import SmartDatalake

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"
path=r"C:\Users\user\AppData\Local\Programs\Python\Python311\Electors Data Summary chardata.xlsx"
path1=r"C:\Users\user\AppData\Local\Programs\Python\Python311\Detailed Results.xlsx"
path2=r"C:\Users\user\AppData\Local\Programs\Python\Python311\Performance of Political Partiesfor chatbot.xlsx"
path3=r"C:\Users\user\AppData\Local\Programs\Python\Python311\Candidates%20Data%20Summary.xlsx"
dataset=pd.read_excel(path1)
dataset.dropna(inplace=True)
df1=pd.DataFrame(dataset)
dataset1 =pd.read_excel(path2)
dataset1.dropna(inplace=True)
df2=pd.DataFrame(dataset1)
dataset2=pd.read_excel(path2)
dataset2.dropna(inplace=True)
df3=pd.DataFrame(dataset2)
dataset3=pd.read_excel(path3)
dataset3.dropna(inplace=True)
df4=pd.DataFrame(dataset3)



st.image("chatbot.gif")
st.title("Here is your Assistant!")
query = st.text_area("Enter your query:")

# Initialize OpenAI LLM and SmartDatalake
llm = OpenAI(api_token=os.environ["OPENAI_API_KEY"])
dl = SmartDatalake([df1,df2,df3,df4], config={"llm": llm})

# Chatbot interaction
if query:
    result = dl.chat(query)
    st.write(result)
