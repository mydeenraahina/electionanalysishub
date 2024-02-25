import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'x1': ["a","b","c","d","e"],
    'x2': ["a","b","c","d","e"],

    'y1': [2, 3, 5, 7, 11],
    
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create the Plotly Express figure
fig = px.line(df, x=['x1','x2'], y='y1')

# Update layout to include zooming
fig.update_layout(
    title="Multiple Line Graphs",
    xaxis_title="X-axis",
    yaxis_title="Y-axis",
    hovermode="x"
)

# Display the plot with Streamlit
st.plotly_chart(fig)
