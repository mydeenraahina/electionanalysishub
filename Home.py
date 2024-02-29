import streamlit as st

# Left column (Featured Visualizations)
# Set page title and background color
st.set_page_config(page_title="Election Data Analysis", page_icon="📊", layout="wide")
with st.sidebar:
    st.success("👆Click the above Option")
st.markdown("<h1 style='color:#ff0066'>🗳️Election Data Analysis!</h1>", unsafe_allow_html=True)
st.markdown("---")
# Main content columns
left_column, right_column = st.columns([1, 1])

with left_column:
    ## Objective:
    st.caption("""Our objective is to provide comprehensive analysis and insights into various aspects of elections.
                We cover topics such as:""")

    st.error(" - Election Nomaination Insights")
    st.error(" - Election related metric")
    st.error(" - Party alliances")
    st.error(" - Electoral Result")

    st.header("📊📈Featured Visualizations")
    st.write("""
    We provide a comprehensive platform for exploring election data and insights. Dive deep into voter turnout, party alliances, and nomination insights to gain valuable perspectives on election trends.
    """)

    st.markdown("---")
    st.image("homepicture2.jpeg")
   
    
# Right column (About and Contact)
with right_column:
    st.image("homepicture.jpeg")
    st.header("📝About")
    st.write("""
    Election Data Analysis is your comprehensive platform for exploring election data and insights.
    Dive deep into voter turnout, party alliances, and nomination insights to gain valuable perspectives on election trends.

    
    """)
