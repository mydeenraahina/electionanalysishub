import os
import streamlit as st
import pandas as pd
from pandasai import SmartDatalake
from requests import get
from pandasai.llm import OpenAI
from pandasai.responses.response_parser import ResponseParser

# Set your OpenAI API key
MY_API_KEY = "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"

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = MY_API_KEY

pd.options.display.max_rows = 300
pd.options.display.max_columns = 8

# Define function to read Excel files
class ReadData:
    @staticmethod
    def read_excel(url, file_name):
        try:
            # Sending a GET request to the URL to retrieve the file content
            retrieve = get(url)

            # Opening the local file in binary write mode and writing the content
            with open(file_name, 'wb') as file:
                file.write(retrieve.content)

            # Reading the Excel file using pandas
            dataset = pd.read_excel(file_name, engine='openpyxl')
        except FileNotFoundError as e1:
            # Print an error message if the file is not found
            print(f"Error: {e1} File not found")
        else:
            # Return the dataset if successfully read
            return dataset

# URLs and file names for the Excel files
urls = {
    "10-Detailed Results": "https://github.com/mydeenraahina/data_set/raw/main/10-%2520Detailed%2520Results%2520(1).xlsx",
    "Electors Data Summary": "https://github.com/mydeenraahina/data_set/raw/main/Electors Data Summary chardata.xlsx",
    "Performance of Political Parties": "https://github.com/mydeenraahina/data_set/raw/main/Performance of Political Partiesfor chatbot.xlsx",
    "Candidates Data Summary": "https://github.com/mydeenraahina/data_set/raw/main/Candidates%2520Data%2520Summarychart.xlsx"
}

file_names = {
    "10-Detailed Results": "10-Detailed_Results.xlsx",
    "Electors Data Summary": "Electors_Data_Summary.xlsx",
    "Performance of Political Parties": "Political_Parties_Performance.xlsx",
    "Candidates Data Summary": "Candidates_Data_Summary.xlsx"
}

# Read Excel files
datasets = {}
for key, value in urls.items():
    datasets[key] = ReadData.read_excel(value, file_names[key])

# Initialize Streamlit
st.set_page_config(
    page_title="Election Analytics Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.image("chatbot.gif")
st.title("Here is your AI Assistant!")
query = st.text_area("Enter your query:")

# Initialize OpenAI LLM
llm = OpenAI(api_token=os.environ["OPENAI_API_KEY"])

# Initialize SmartDatalake
dl = SmartDatalake(list(datasets.values()), config={"llm": llm, "response_parser": ResponseParser})

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
