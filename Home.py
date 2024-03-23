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
    

    st.header("📊📈Featured Visualizations")
    st.write("""
   Discover a comprehensive platform for exploring election data and gaining insights. Delve into voter turnout, party alliances, and nomination insights to uncover valuable perspectives on election trends.
    """)

    st.markdown("---")
    st.image("homepicture (3).png")
    import streamlit as st

st.caption("""Our objective is to provide comprehensive analysis and insights into various aspects of elections.
                We cover topics such as:""")

st.info(" - Election Nomination Insights")
st.info(" - Election-related metrics")
st.info(" - Party alliances")
st.info(" - Candidates Details")
st.info(" - Electoral Results")

# Add AI chat facility introduction
st.markdown("""
    ### AI Chat Facility
    
    Need assistance or have questions? Our AI assistant is here to help! Simply type your query in the chat box below and get instant answers and insights.
""")

st.title("Happy Exploring!...") 
    
# Right column (About and Contact)
with right_column:
    st.image("homepicture2.png")
    st.header("📝About")
    st.write("""
    This Election Data Analysis, your hub for election insights. Explore voter turnout, party alliances, Candidates Details,Elction Result and nomination trends. Meet our AI assistant for personalized assistance and deeper insights. Ask questions, get clarifications, and navigate election dynamics effortlessly!.  """)
    
