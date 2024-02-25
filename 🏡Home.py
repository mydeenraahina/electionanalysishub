import streamlit as st
from streamlit_extras.tags import tagger_component

# Display tags with a separate button
tagger_component(
    "Here are colored tags",
    ["Total Votes Casted 2021"],
    color_name=["orange"]
)

st.markdown(
    """
    <style>
    .stButton>button {
        border: none !important;
        background-color: orange !important;
        color: darkcyan !important;
        border-radius: 20px !important; /* Adjust the value to change the roundness */
        padding: 8px 16px !important; /* Adjust the padding to fit the content */
        font-size: 14px !important; /* Adjust the font size */
    }
    </style>
    """,
    unsafe_allow_html=True
)


