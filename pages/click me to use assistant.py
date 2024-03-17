import streamlit as st
import pandas as pd
from pandasai import SmartDatalake
from requests import get

# Set Streamlit page configuration
st.set_page_config(
    page_title="Election Analytics Hub!",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define URLs for the Excel files
url1 = "https://github.com/mydeenraahina/data_set/raw/main/Detailed%20Results.xlsx"
url2 = "https://github.com/mydeenraahina/data_set/raw/main/Electors Data Summary chardata.xlsx"
url3 = "https://github.com/mydeenraahina/data_set/raw/main/Performance of Political Partiesfor chatbot.xlsx"

# Define function to read Excel data
@st.cache
def read_excel_data(url, file_name):
    try:
        # Sending a GET request to the URL to retrieve the file content
        retrieve = get(url)
        # Opening the local file in binary write mode and writing the content
        with open(file_name, 'wb')as file:
            file.write(retrieve.content)
        # Reading the Excel file using pandas
        dataset = pd.read_excel(file_name, engine='openpyxl')
    except FileNotFoundError as e1:
        # Print an error message if the file is not found
        st.error(f"Error: {e1} File not found")
    else:
        # Return the dataset if successfully read
        return dataset

# Read Excel data
dataset1 = read_excel_data(url1, "Detailed Results.xlsx")
dataset2 = read_excel_data(url2, "Electors Data Summary chardata.xlsx")
dataset3 = read_excel_data(url3, "Performance of Political Partiesfor chatbot.xlsx")

# Initialize SmartDatalake
datalake = SmartDatalake([dataset1, dataset2, dataset3])

# Retrieve OpenAI API key from Streamlit secrets
openai_api_key = st.secrets["openai_api_key"]

# Initialize OpenAI with the API key
llm = OpenAI(api_token=openai_api_key)

st.image("chatbot.gif")
st.title("Here is your AI Assistant!")
query = st.text_area("Enter your query:")

# Chatbot interaction
if query:
    result = datalake.chat(query, config={"llm": llm})
    st.write("User (you): " + query)
    st.write("AI Assistant: " + result)
