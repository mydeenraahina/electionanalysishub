from pandasai.llm import OpenAI 
import os
import streamlit as st
import pandas as pd
from pandasai import SmartDatalake
from requests import get
import openpyxl
import webbrowser
st.set_page_config(
    page_title="Election Analytics Hub!",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
   
)
# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

pd.options.display.max_rows = 300
pd.options.display.max_columns = 8


# URLs for the Excel files
url1 = "https://github.com/mydeenraahina/data_set/raw/main/10-%2520Detailed%2520Results%2520(1).xlsx"
ur12="https://github.com/mydeenraahina/data_set/raw/main/Electors Data Summary chardata.xlsx"
url3="https://github.com/mydeenraahina/data_set/raw/main/Performance of Political Partiesfor chatbot.xlsx"
url4="https://github.com/mydeenraahina/data_set/raw/main/Candidates%2520Data%2520Summarychart.xlsx"


file_1 = "10-%2520Detailed%2520Results%2520(1).xlsx"
file_2 = "Electors Data Summary chardata.xlsx"
file_3 = "Performance of Political Partiesfor chatbot.xlsx"
file_4="Candidates%2520Data%2520Summarychart.xlsx"
class Read_Data():
    # Setting display options for Pandas
    pd.options.display.max_rows = 150
    pd.options.display.max_columns = 8

    @staticmethod
    def Read_Excel(url,file_name):
        try:
            # Sending a GET request to the URL to retrieve the file content
            retrieve = get(url)

            # Opening the local file in binary write mode and writing the content
            with open(file_name, 'wb')as file:
              file.write(retrieve.content)

            # Reading the Excel file using pandas
            dataset = pd.read_excel(file_name,engine='openpyxl')
        except FileNotFoundError as e1:
            # Print an error message if the file is not found
            print(f"Error: {e1} File not found")
        else:
            # Return the dataset if successfully read
            return dataset

# Dataset 1: Electors Data Summary
dataset0 = Read_Data.Read_Excel(url1,file_1)
dataset1 = Read_Data.Read_Excel(ur12,file_2)
dataset2 = Read_Data.Read_Excel(url3,file_3)
dataset3=Read_Data.Read_Excel(url4,file_4)

class Streamlitresponse(ResponseParser):
    def __init__(self, context):
        super().__init__(context)

    def format_dataframe(self, result):
        st.dataframe(result["value"])

    def format_plot(self, result):
        st.write("AI Assistant:")
        st.image(result["value"],width=700)

    def format_other(self, result):
        st.write(result["value"])

st.set_page_config(
    page_title="Election Analytics Hub!",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.image("chatbot.gif")
st.title("Here is your AI Assistant!")
query = st.text_area("Enter your query:")

# Initialize OpenAI LLM and SmartDatalake
llm = OpenAI(api_token=os.environ["OPENAI_API_KEY"])

df1 = pd.DataFrame(dataset0).dropna()


df2 = pd.DataFrame(dataset1).dropna()


df3 = pd.DataFrame(dataset2).dropna()

df4=pd.DataFrame(dataset3).dropna()


# Initialize SmartDatalake
dl = SmartDatalake([df1, df2, df3,df4], config={"llm": llm, "response_parser": Streamlitresponse})

# Chatbot interaction
if st.button("Submit", key="primary", help="Submit query"):
    result = dl.chat(query)
    st.write("User(you): ", query)
    st.write(result)

# Apply CSS to the button for styling
st.markdown(
    """
    <style>
    div[data-testid="stButton"] button {
        background-color: #007bff !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
