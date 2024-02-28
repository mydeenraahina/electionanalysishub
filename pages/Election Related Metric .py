from requests import get
import pandas as pd
import openpyxl
import os
import webbrowser
import streamlit as st
import plotly.express as px
import time
from datetime import datetime

st.set_page_config(
    page_title="Election Analytics Hub!",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
   
)





url1 = "https://github.com/mydeenraahina/data_set/raw/main/Electors%20Data2.xlsx"

url3= "https://github.com/mydeenraahina/data_set/raw/main/10-%20Detailed%20Results%20(1).xlsx"

file_1 = "Electors%20Data2.xlsx"

file_3="10-%20Detailed%20Results%20(1).xlsx"

class Read_Data():
    # Setting display options for Pandas
    pd.options.display.max_rows = 150
    pd.options.display.max_columns = 8

    @staticmethod
    def Read_Excel(url, file_name):
        try:
            retrieve = get(url)

            with open(file_name, 'wb')as file:
              file.write(retrieve.content)

            dataset = pd.read_excel(file_name,engine='openpyxl')
        except FileNotFoundError as e1:
            print(f"Error: {e1} File not found")
        else:
            return dataset
dataset1 = Read_Data.Read_Excel(url1,file_1)
dataset4 = Read_Data.Read_Excel(url3,file_3)
class Clean_Dataset1:

    def removing_empty_val(self, dataset):
        dataset.dropna(inplace=True)

    def removing_duplicates(self, dataset):
        dataset.drop_duplicates(inplace=True)

    def setting_index(self, dataset):
        index_name = 'Election-related metrics'
        dataset.set_index(index_name, inplace=True)

    def cleaned_data(self, dataframe):
  
        dataset = dataframe

        # Apply cleaning steps

        self.removing_empty_val(dataset)
        self.removing_duplicates(dataset)
        self.setting_index(dataset)

        # Return the cleaned dataset
        return dataset


cleaned_dataset1=Clean_Dataset1()
dataset1_cleaned=cleaned_dataset1.cleaned_data(dataset1)
print(dataset1_cleaned)
pd.options.display.max_rows = 300
pd.options.display.max_columns = 8


class Clean_Dataset4:

    
    
    def setting_index(self, dataset):
        dataset.set_index('AC NAME', inplace=True)
    def removing_empty_val(self, dataset):
        # Removing empty values
        dataset.dropna(inplace=True)


    def cleaned_data(self, dataframe):
        dataset = dataframe

        
        
        
        self.setting_index(dataset)
        self.removing_empty_val(dataset)
        # Return the cleaned dataset
        return dataset


cleaned_dataset4=Clean_Dataset4()
dataset4_cleaned=cleaned_dataset4.cleaned_data(dataset4)

st.markdown("<h1 style='color:#ff0066' ;> 📊 ELECTION RELATED METRICS!</h1>", unsafe_allow_html=True)
st.write("💡 Explore detailed insights and metrics about the voters Turnout  Tamilnadu election 2021.")

col1, col2,col3=st.columns(3)
with col1:
    st.title(" Get Started!")
    st.write("🗳️ Explore insights into election nominations. Click on the metric below to delve into the analysis!")

    
    

   


with col2:
    st.image("picture1.png",width=200)

def voters_cat(val):
    gen_voters = dataset1_cleaned.loc[val]['GEN']
    sc_voters=dataset1_cleaned.loc[val]['SC']
    st_voters=dataset1_cleaned.loc[val]['ST']
    total_voters=gen_voters+sc_voters+st_voters
    voters=["Total voters","GEN","SC","ST"]
    no_of_voters=[total_voters,gen_voters,sc_voters,st_voters]
    total_voters= pd.DataFrame({'Category':voters, 'Total_voters': no_of_voters})
    trans = total_voters.transpose()
    st.dataframe(trans)
    fig = px.bar(total_voters, x='Category', y='Total_voters',color_discrete_sequence=['cyan'])
    st.write(fig)
def voters_caste_catey(value):
     male=dataset1_cleaned.loc["MALE voters"][value]
     female=dataset1_cleaned.loc["FEMALE voters"][value]
     third_gender=dataset1_cleaned.loc["THIRD GENDER voters"][value]
     total_voters=dataset1_cleaned.loc["TOTAL voters"][value]
     caste_category=["MALE","FEMALE","THIRD GENDER","TOTAL VOTERS"]
     voters=[male,female,third_gender,total_voters]
     df=pd.DataFrame({f'{value}category':caste_category,'voters':voters})
     st.dataframe(df)
     fig = px.bar(df, x=f'{value}category', y='voters',color_discrete_sequence=['indigo'])
     st.write(fig)

    


def total_voters_gender():
    Total_male_voters = dataset1_cleaned.loc['MALE voters'].sum()
    Total_female_voters = dataset1_cleaned.loc['FEMALE voters'].sum()
    Total_transgender_voters = dataset1_cleaned.loc['THIRD GENDER voters'].sum()
    Total_voters = Total_male_voters+Total_female_voters+Total_transgender_voters
    gender = ["Total voters","Male", "Female", "Third gender"]
    voters = [Total_voters,Total_male_voters, Total_female_voters, Total_transgender_voters ]
    Total_voter_genderwise = pd.DataFrame({"Gender": gender, "Total Voters": voters})
    trans=Total_voter_genderwise.transpose()
    st.dataframe(trans)
    fig=px.bar(Total_voter_genderwise,x='Gender',y='Total Voters',color_discrete_sequence=['hotpink'])
    st.write(fig)
import streamlit as st

# Instructions for users
st.info("""This  allows you to explore different aspects of the Tamil Nadu 2021 election
           To get started, expand the section below 👇🏼 and click 🖱️ on the buttons to view specific metricsand analyses📊.""")
# Define CSS style for buttons
button_style = """
<style>
.stButton>button {
    border: none !important;
    background-color: #ff0066; /* Tomato */
    color: #FFFFFF !important; /* White */
    border-radius: 20px !important; /* Adjust the value to change the roundness */
    padding: 8px 16px !important; /* Adjust the padding to fit the content */
    font-size: 14px !important; /* Adjust the font size */
}
</style>
"""

# Render the CSS style
st.markdown(button_style, unsafe_allow_html=True)

# Define buttons with numbering, icons, and explanatory text
with st.expander("🔍 Explore different aspects of the Tamil Nadu 2021 📈 election"):
    
    unique_districts = dataset4_cleaned.index.unique().tolist()
    st.markdown("<h4 style='color:#ff0066' ;> 🎯 Election Turnout Over 234 Constituencies Tamilnadu 2021</h4>", unsafe_allow_html=True)

       

    st.write("This tool allows you to analyze election turnout data Over 234 Constituencies. Please select one or more districts/Constituence from the dropdown menu below:")
    # Multi-select box for district selection
    selected_districts = st.multiselect('Select District(s)', unique_districts)

    # Function to calculate and display district-wise turnout
    def district_wise_turnout(district):
        total_general = dataset4_cleaned.loc[district]["GENERAL"].sum()
        total_postal = dataset4_cleaned.loc[district]["POSTAL"].sum()
        total_votes = dataset4_cleaned.loc[district]["TOTAL"].sum()
        total_voters = dataset4_cleaned.loc[district]["TOTAL ELECTORS"].sum()
            
        # Creating a DataFrame for the turnout data
        turnout_data = {
                "Category": ["General Votes", "Postal Votes", "Total Votes", "Total Voters"],
                "Votes": [total_general, total_postal, total_votes, total_voters]
            }
        turnout_df = pd.DataFrame(turnout_data)

        # Displaying the DataFrame using Streamlit
        st.subheader(f"Turnout for {district}")
        st.dataframe(turnout_df)

        # Plotting a pie chart using Plotly Express
        fig = px.line(turnout_df, x='Category', y='Votes', color_discrete_sequence=['darkcyan'])
        st.plotly_chart(fig)


    for district in selected_districts:
        district_wise_turnout(district)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("🎯 Total Eligible Voters Tamilnadu 2021", unsafe_allow_html=True)
        button1 = st.button("Click to View", key="button1", type="primary")
        st.markdown("🎯 Total Votes Casted Tamilnadu 2021", unsafe_allow_html=True)
        button2 = st.button("Click to View", key="button2", type="primary")
        st.markdown("🎯 Voters Turnout Over 234 constituency  Tamilnadu 2021", unsafe_allow_html=True)
        button3= st.button("Click to View", key="button3", type="primary")
        st.markdown("🎯 Examining Poll Percentage Trends TN 2021", unsafe_allow_html=True)
        button4 = st.button("Click to View", key="button4", type="primary")

        st.markdown("🎯 Gender Gap in Different Castes in Voter Turnout", unsafe_allow_html=True)
        button5 = st.button("Click to View", key="button5", type="primary")

        
    with col2:
        
        st.markdown("🎯 Gender gap in different Castes votes polled TN 2021", unsafe_allow_html=True)
        button6 = st.button("Click to View", key="button6", type="primary")
        st.markdown("🎯 The Role of Polling Stations TN Election 2021", unsafe_allow_html=True)
        button7 = st.button("Click to View", key="button7", type="primary")

        st.markdown("🎯 Average No. of Electors per Polling Station TN Election 2021", unsafe_allow_html=True)
        button8 = st.button("Click to View", key="button8", type="primary")
        st.markdown("🎯 Election Outcome Analysis: Voter Turnout TN Election 2021", unsafe_allow_html=True)
        button9 = st.button("Click to View", key="button9", type="primary")

        st.markdown("🎯 Overall Voter Participation and Election Efficiency TN Election 2021", unsafe_allow_html=True)
        button10 = st.button("Click to View", key="button10", type="primary")


    if button1:
        st.markdown("<h1 style='color: gray';> Total Eligible Voters TN 2021</h1>", unsafe_allow_html=True)
        st.caption("Click here to find out the total eligible voters in the Tamil Nadu 2021 election!")
    
        tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8= st.tabs(["TOTAL MALE VOTERS BY CATEGORY", "TOTAL FEMALE VOTERS BY CATEGORY", "TOTAL THIRD GENDER VOTERS ACROSS CATEGORY","TOTAL NO.OF VOTERS GENDER-WISE","TOTAL GEN CATEGORY VOTERS","TOTAL SC CATEGORY VOTERS","TOTAL ST CATEGORY VOTERS","TOTAL VOTERS ACROSS CATEGORY"])
        
        with tab1:
            voters_cat("MALE voters")
        with tab2:
            voters_cat("FEMALE voters")
        with tab3:
            voters_cat("THIRD GENDER voters")
        with tab4:
            total_voters_gender()
        with tab5:
            voters_caste_catey('GEN')
        with tab6:
            voters_caste_catey('SC')
        with tab7:
            voters_caste_catey('ST')
        with tab8:
            voters_cat("TOTAL voters" )



    def votes_cast(val):

            voted_gen = dataset1_cleaned.loc[val]['GEN']
            voted_sc = dataset1_cleaned.loc[val]['SC']
            voted_st = dataset1_cleaned.loc[val]['ST']
            total_votes_21=voted_gen+voted_sc+voted_st
            votes=["TOTAL VOTES","GEN","SC","ST"]
            voted_values=[total_votes_21,voted_gen,voted_sc,voted_st]
            votes_21 = pd.DataFrame({'Category': votes, 'Total_votes': voted_values})
            trans = votes_21.transpose()
            st.dataframe(trans)
            fig = px.bar(votes_21, x='Category', y='Total_votes',color_discrete_sequence=['DarkMagenta'])
            st.write(fig)
    def votes_caste_catey(value):
        male=dataset1_cleaned.loc["voted MALE"][value]
        female=dataset1_cleaned.loc["voted FEMALE"][value]
        third_gender=dataset1_cleaned.loc["voted THIRD GENDER"][value]
        caste_category=["MALE","FEMALE","THIRD GENDER","TOTAL VOTES"]
        votes=[male,female,third_gender]
        votes.append(sum(votes))
        df=pd.DataFrame({f'{value}category':caste_category,'votes':votes})
        st.dataframe(df)
        fig = px.bar(df, x=f'{value}category', y='votes',color_discrete_sequence=['indianred'])
        st.write(fig)      
    def votes_genderwise():
            Total_male_votes = dataset1_cleaned.loc['voted MALE'].sum()
            Total_female_votes = dataset1_cleaned.loc['voted FEMALE'].sum()
            Total_transgender_votes = dataset1_cleaned.loc['voted THIRD GENDER'].sum()
            Total_votes = Total_male_votes+Total_female_votes+Total_transgender_votes
            gender = ["Total votes","Male", "Female", "Third gender"]
            votes = [Total_votes,Total_male_votes, Total_female_votes, Total_transgender_votes ]
            Total_votes_genderwise = pd.DataFrame({"Gender": gender, "Total Votes": votes})
            trans=Total_votes_genderwise.transpose()
            st.dataframe(trans)
            fig=px.bar(Total_votes_genderwise,x='Gender',y='Total Votes',color_discrete_sequence=['hotpink'])
            st.write(fig)
    def total_votes_cast():
            total_votes_GEN = (dataset1_cleaned.loc['voted MALE']['GEN'] +dataset1_cleaned.loc['voted FEMALE']['GEN'] +dataset1_cleaned.loc['voted THIRD GENDER']['GEN'] +dataset1_cleaned.loc['POSTAL votes']['GEN'] +dataset1_cleaned.loc['NOTA VOTES']['GEN'])
            total_votes_SC = (dataset1_cleaned.loc['voted MALE']['SC'] +dataset1_cleaned.loc['voted FEMALE']['SC'] + dataset1_cleaned.loc['voted THIRD GENDER']['SC'] + dataset1_cleaned.loc['POSTAL votes']['SC'] + dataset1_cleaned.loc['NOTA VOTES']['SC'])
            total_votes_ST = (dataset1_cleaned.loc['voted MALE']['ST'] +dataset1_cleaned.loc['voted FEMALE']['ST'] +dataset1_cleaned.loc['voted THIRD GENDER']['ST'] +dataset1_cleaned.loc['POSTAL votes']['ST'] +dataset1_cleaned.loc['NOTA VOTES']['ST'])
            total_votes_polled_21=total_votes_GEN+total_votes_SC+total_votes_ST
            category = ['total_votes_polled','total_votes_GEN', 'total_votes_SC', 'total_votes_ST']
            votes = [total_votes_polled_21,total_votes_GEN, total_votes_SC, total_votes_ST]
            total_vote_category_wise = pd.DataFrame({'category':category  , 'total_votes': votes})
            trans = total_vote_category_wise.transpose()
            st.dataframe(trans)
            fig = px.bar(total_vote_category_wise, x='category', y='total_votes',color_discrete_sequence=['forestgreen'])
            st.write(fig)

    if button2:
        st.markdown("<h1 style='color: gray';> Total Votes casted : Tamil Nadu 2021</h1>", unsafe_allow_html=True)
        st.caption("Click here to know the total votes cast in the Tamil Nadu 2021 election!")
        tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10= st.tabs(["TOTAL  MALES VOTES BY CATEGORY", "TOTAL  FEMALES VOTES BY CATEGORY", "TOTAL   THIRD GENDERS  VOTES BY CATEGORY",
                    "TOTAL VOTES POLLED GENDER_WISE","TOTAL POSTAL VOTES","TOTAL NOTA VOTES","TOTAL GEN CATEGORY VOTES POLLED","TOTAL SC CATEGORY VOTES POLLED","TOTAL ST CATEGORY VOTES POLLED","TOTAL VOTES POLLED BY CATEGORY TN 21"])
        
        with tab1:
                
            votes_cast("voted MALE")
        with tab2:
                
            votes_cast("voted FEMALE")
        with tab3:
                
            votes_cast("voted THIRD GENDER")
        with tab4:
            votes_genderwise()
        with tab5:       
            votes_cast("POSTAL votes")
        with tab6:
            
            votes_cast("NOTA VOTES")
        with tab7:
            votes_caste_catey('GEN')
        with tab8:
            votes_caste_catey('SC')
        with tab9:
            votes_caste_catey('ST')
        with tab10:
                
            total_votes_cast()


    def poll_percentage_by_category(Type):
            poll = dataset1_cleaned.loc['POLL PERCENTAGE'][Type]
            return poll
        
    def poll_percentage():
            categories = ["GEN", "SC", "ST"]
            total = 0
            poll_values = [poll_percentage_by_category(category) for category in categories]
            total = sum(poll_values)

            categories.insert(0, "TOTAL")
            poll_values.insert(0, total)
            st.subheader(" Examining Poll Percentage Trends in 2021")
            st.caption("""In 2021, the global landscape saw a varied turnout in electoral events,
                                shaping political narratives worldwide. The "POLL PERCENTAGE 2021"
                                encapsulated the pulse of democracy, reflecting voter engagement amidst
                                unprecedented challenges such as the ongoing pandemic and political transitions.
                                Technological advancements, including digital campaigns and online registration drives,
                                played pivotal roles in mobilizing voters and influencing turnout rates. Analysis of the
                                data revealed intricate patterns, shedding light on demographic disparities and
                                socio-economic factors impacting participation. Understanding these trends is
                                crucial for policymakers to devise inclusive strategies and fortify democratic processes.""")

            total_poll = pd.DataFrame({"category": categories, "votes": poll_values})
            trans=total_poll.transpose()
            st.write("Poll Percentage TN ELECTION  2021 by category ")
            st.dataframe(trans)
            fig = px.area(total_poll, x='category', y='votes',color_discrete_sequence=['LawnGreen'],title="Representation Poll Percentage Trends in 2021 by category ")
            st.write(fig)
    # Assuming your dataset is stored in a variable named 'dataset4_cleaned'
    # Get the unique index values

    
    if button4:
        st.markdown("<h1 style='color: gray';> Examining Poll Percentage Trends in 2021</h1>", unsafe_allow_html=True)
        st.caption("""In 2021, the global landscape saw a varied turnout in electoral events, shaping political narratives worldwide.
                            The "POLL PERCENTAGE 2021" encapsulated the pulse of democracy, reflecting voter engagement amidst
                            unprecedented challenges such as the ongoing pandemic and political transitions. Technological advancements,
                            including digital campaigns and online registration drives, played pivotal roles in mobilizing voters and influencing turnout rates.
                            Analysis of the data revealed intricate patterns, shedding light on demographic disparities and socio-economic factors impacting participation.
                            Understanding these trends is crucial for policymakers to devise inclusive strategies and fortify democratic processes.""")
        poll_percentage()



    def no_of_polling_stataions(Type):
            poll = dataset1_cleaned.loc['NO. OF POLLING STATIONS'][Type]
            return poll
        
    def polling_station():
            categories = ["GEN", "SC", "ST"]
            total = 0
            poll_values = [no_of_polling_stataions(category) for category in categories]
            total = sum(poll_values)

            categories.insert(0, "TOTAL")
            poll_values.insert(0, total)
            st.subheader(" Mapping Democracy: Understanding the Role of Polling Stations TN 2021")
            st.caption("""The number of polling stations acts as a vital measure of electoral accessibility and engagement.
                                Trends in this metric offer insights into the effectiveness of electoral infrastructure and the ability
                                of citizens to participate in democratic processes. By examining variations in polling station distribution,
                                we gain valuable perspectives on geographical disparities, demographic considerations, and the challenges
                                of ensuring equitable voting opportunities. Understanding these dynamics is crucial for fostering inclusive
                                elections and strengthening the foundations of democracy.""")
            st.write("No.of polling station by category TN 2021")
            total_poll = pd.DataFrame({"category": categories, "votes": poll_values})
            trans=total_poll.transpose()
            st.dataframe(trans)
            fig = px.area(total_poll, x='category', y='votes',color_discrete_sequence=['LightCoral'],title="Representing No.of polling station by category TN 2021")
            st.write(fig)
    if button5:
        def gen_voters_turnout():
                gen_voters=["MALE voters","FEMALE voters","THIRD GENDER voters","TOTAL voters"]
                gen_votes=[]
                for val in gen_voters:
                    gen_votes_data = dataset1_cleaned.loc[val]['GEN']
                    gen_votes.append(gen_votes_data)
                total_voters=pd.DataFrame({"category":gen_voters,"votes":gen_votes})
                trans=total_voters.transpose()
                st.dataframe(trans)
                fig=px.line(total_voters,x='category',y='votes',color_discrete_sequence=['DarkMagenta'])
                st.plotly_chart(fig)
        def sc_voters_turnout():
                sc_voters=["MALE voters","FEMALE voters","THIRD GENDER voters","TOTAL voters"]
                sc_votes=[]
                for val in sc_voters:
                    sc_votes_data = dataset1_cleaned.loc[val]['SC']
                    sc_votes.append(sc_votes_data)
                total_voters=pd.DataFrame({"category":sc_voters,"votes":sc_votes})
                trans=total_voters.transpose()
                st.dataframe(trans)
                fig=px.line(total_voters,x='category',y='votes',color_discrete_sequence=['DarkOrange'])
                st.plotly_chart(fig)
                
        def st_voters_turnout():
                st_voters=["MALE voters","FEMALE voters","THIRD GENDER voters","TOTAL voters"]
                st_votes=[]
                for val in st_voters:
                    st_votes_data = dataset1_cleaned.loc[val]['ST']
                    st_votes.append(st_votes_data)
                total_voters=pd.DataFrame({"category":st_voters,"votes":st_votes})
                trans=total_voters.transpose()
                st.dataframe(trans)
                fig=px.line(total_voters,x='category',y='votes',color_discrete_sequence=['indianred'])
                st.plotly_chart(fig)



        st.markdown("<h1 style='color: gray';>Gender gap in different category [GEN,SC,ST] in voters turout TN 2021</h1>", unsafe_allow_html=True)
        st.caption("Click here to know the Gender gap in different category [GEN,SC,ST] in voters turout in the Tamil Nadu 2021 election!")
        tab1, tab2, tab3= st.tabs(["Gender Gap in GEN Voter Turnout", "Gender Gap in SC Voter Turnout", "Gender Gap in ST Voter Turnout"])
    
        with tab1:
            gen_voters_turnout()
        with tab2:
                
            sc_voters_turnout()
        with tab3:
                
            st_voters_turnout()
        


    def gen_votes_polled():
        male= dataset1_cleaned.loc['voted MALE']['GEN']
        female=dataset1_cleaned.loc['voted FEMALE']['GEN']
        third_gender=dataset1_cleaned.loc['voted THIRD GENDER']['GEN']
        postal=dataset1_cleaned.loc['POSTAL votes']['GEN']
        nota=dataset1_cleaned.loc['NOTA VOTES']['GEN']
        gen_votes = ["MALE VOTES","FEMALE VOTES","THIRDGENDER VOTES","POSTAL VOTES","NOTA VOTES","TOTAL VOTES"]
        
        votes=[male,female,third_gender,postal,nota]
        votes.append(sum(votes))
        total_voters=pd.DataFrame({"category":gen_votes,"votes":votes})
        trans=total_voters.transpose()
        st.dataframe(trans)
        fig=px.line(total_voters,x='category',y='votes',color_discrete_sequence=['DarkMagenta'])
        st.plotly_chart(fig)
    def sc_votes_polled():
        male= dataset1_cleaned.loc['voted MALE']['SC']
        female=dataset1_cleaned.loc['voted FEMALE']['SC']
        third_gender=dataset1_cleaned.loc['voted THIRD GENDER']['SC']
        postal=dataset1_cleaned.loc['POSTAL votes']['SC']
        nota=dataset1_cleaned.loc['NOTA VOTES']['SC']
        sc_votes = ["MALE VOTES","FEMALE VOTES","THIRDGENDER VOTES","POSTAL VOTES","NOTA VOTES","TOTAL VOTES"]
        
        votes=[male,female,third_gender,postal,nota]
        votes.append(sum(votes))
        total_voters=pd.DataFrame({"category":sc_votes,"votes":votes})
        trans=total_voters.transpose()
        st.dataframe(trans)
        fig=px.line(total_voters,x='category',y='votes',color_discrete_sequence=['DarkMagenta'])
        st.plotly_chart(fig)

    def st_votes_polled():
        male= dataset1_cleaned.loc['voted MALE']['ST']
        female=dataset1_cleaned.loc['voted FEMALE']['ST']
        third_gender=dataset1_cleaned.loc['voted THIRD GENDER']['ST']
        postal=dataset1_cleaned.loc['POSTAL votes']['ST']
        nota=dataset1_cleaned.loc['NOTA VOTES']['ST']
        st_votes = ["MALE VOTES","FEMALE VOTES","THIRDGENDER VOTES","POSTAL VOTES","NOTA VOTES","TOTAL VOTES"]
        
        votes=[male,female,third_gender,postal,nota]
        votes.append(sum(votes))
        total_voters=pd.DataFrame({"category":st_votes,"votes":votes})
        trans=total_voters.transpose()
        st.dataframe(trans)
        fig=px.line(total_voters,x='category',y='votes',color_discrete_sequence=['DarkMagenta'])
        st.plotly_chart(fig)




    if button6:
        st.markdown("<h1 style='color: gray';>Gender gap in different category [GEN,SC,ST] in toatl votes polled TN 2021</h1>", unsafe_allow_html=True)
        st.caption("Click here to know the Gender gap in different category [GEN,SC,ST] in total votes polled in the Tamil Nadu 2021 election!")
        tab1, tab2, tab3= st.tabs(["Gender Gap in GEN Votes ", "Gender Gap in SC Votes ", "Gender Gap in ST Votes "])
    
        with tab1:
            gen_votes_polled()
        with tab2:
                
            sc_votes_polled()
        with tab3:
                
            st_votes_polled()
        

        
        

    if button7:
        st.markdown("<h1 style='color: gray';> Mapping Democracy: Understanding the Role of Polling Stations TN 2021</h1>", unsafe_allow_html=True)
        st.caption("""The number of polling stations acts as a vital measure of electoral accessibility and engagement.
                            Trends in this metric offer insights into the effectiveness of electoral infrastructure and the ability
                            of citizens to participate in democratic processes. By examining variations in polling station distribution,
                            we gain valuable perspectives on geographical disparities, demographic considerations, and the challenges
                            of ensuring equitable voting opportunities. Understanding these dynamics is crucial for fostering inclusive
                            elections and strengthening the foundations of democracy.""")
        polling_station()

    def electors_stations(Type):
            poll = dataset1_cleaned.loc['Average no of electors per polling stations'][Type]
            return poll
        
    def average_polling():
            categories = ["GEN", "SC", "ST"]
            total = 0
            poll_values = [electors_stations(category) for category in categories]
            total = sum(poll_values)

            categories.insert(0, "TOTAL")
            poll_values.insert(0, total)
            
            st.write("Average Number of Electors per Polling Station by category ")
            total_poll = pd.DataFrame({"category": categories, "votes": poll_values})
            trans=total_poll.transpose()
            st.dataframe(trans)
            fig = px.area(total_poll, x='category', y='votes',color_discrete_sequence=['MediumVioletRed'],title="Represending Average Number of Electors per Polling Station by category TN 2021")
            st.write(fig)

    if button8:
        st.markdown("<h1 style='color: gray';> Demographic Density: Exploring the Average Number of Electors per Polling Station</h1>", unsafe_allow_html=True)
        st.caption("""The average number of electors per polling station serves as a key indicator of electoral efficiency and voter access.
                            This metric offers insights into the distribution of electoral resources and the capacity of polling stations to accommodate
                            voter turnout. By analyzing variations in this average across different regions and demographic groups, we gain valuable
                            perspectives on electoral inclusivity and the challenges of ensuring equitable representation. Understanding these dynamics
                            is essential for optimizing electoral processes and enhancing democratic participation""")
        average_polling()



    
    def valid_rej_total():
            
                total_votes_GEN = (dataset1_cleaned.loc['voted MALE']['GEN'] +dataset1_cleaned.loc['voted FEMALE']['GEN'] +dataset1_cleaned.loc['voted THIRD GENDER']['GEN'] +dataset1_cleaned.loc['POSTAL votes']['GEN'] +dataset1_cleaned.loc['NOTA VOTES']['GEN'])
                total_votes_SC = (dataset1_cleaned.loc['voted MALE']['SC'] +dataset1_cleaned.loc['voted FEMALE']['SC'] + dataset1_cleaned.loc['voted THIRD GENDER']['SC'] + dataset1_cleaned.loc['POSTAL votes']['SC'] + dataset1_cleaned.loc['NOTA VOTES']['SC'])
                total_votes_ST = (dataset1_cleaned.loc['voted MALE']['ST'] +dataset1_cleaned.loc['voted FEMALE']['ST'] +dataset1_cleaned.loc['voted THIRD GENDER']['ST'] +dataset1_cleaned.loc['POSTAL votes']['ST'] +dataset1_cleaned.loc['NOTA VOTES']['ST'])
                total_votes_polled_21=total_votes_GEN+total_votes_SC+total_votes_ST
                total_votes_rejected=dataset1_cleaned.loc['votes rejected'].sum()
                total_valid_votes=dataset1_cleaned.loc['valid votes'].sum()
                category=["TOATL VOTES POLLED TN 21","TOTAL REJECTED VOTES TN 21","TOTAL VALID VOTES TN 21"]
                votes=[total_votes_polled_21,total_votes_rejected,total_valid_votes]
                total_votes = pd.DataFrame({"category": category, "votes": votes})
                trans=total_votes.transpose()
                st.dataframe(trans)
                fig = px.area(total_votes, x='category', y='votes',color_discrete_sequence=['Indigo'])
                st.write(fig)
    def total_voters():
        male = dataset1_cleaned.loc['MALE voters'].sum()
        female = dataset1_cleaned.loc['FEMALE voters'].sum()
        third_gender = dataset1_cleaned.loc['THIRD GENDER voters'].sum()
        total = dataset1_cleaned.loc['TOTAL voters'].sum()

        # Create the dictionary for total_voters
        total_voters = {
        "voters": ["MALE VOTERS", "FEMALE VOTERS", "THIRD GENDER VOTERS", "TOTAL VOTERS"],
        "votes": [male, female, third_gender, total]  # Corrected this line
        }   

        # Create DataFrame from total_voters dictionary
        df = pd.DataFrame(total_voters)

        # Display DataFrame
        st.dataframe(df)

        # Create pie chart
        fig = px.pie(df, values='votes', names='voters')
        st.plotly_chart(fig)

    def toatl_votes():
                total_votes_GEN = (dataset1_cleaned.loc['voted MALE']['GEN'] +dataset1_cleaned.loc['voted FEMALE']['GEN'] +dataset1_cleaned.loc['voted THIRD GENDER']['GEN'] +dataset1_cleaned.loc['POSTAL votes']['GEN'] +dataset1_cleaned.loc['NOTA VOTES']['GEN'])
                total_votes_SC = (dataset1_cleaned.loc['voted MALE']['SC'] +dataset1_cleaned.loc['voted FEMALE']['SC'] + dataset1_cleaned.loc['voted THIRD GENDER']['SC'] + dataset1_cleaned.loc['POSTAL votes']['SC'] + dataset1_cleaned.loc['NOTA VOTES']['SC'])
                total_votes_ST = (dataset1_cleaned.loc['voted MALE']['ST'] +dataset1_cleaned.loc['voted FEMALE']['ST'] +dataset1_cleaned.loc['voted THIRD GENDER']['ST'] +dataset1_cleaned.loc['POSTAL votes']['ST'] +dataset1_cleaned.loc['NOTA VOTES']['ST'])
                total_votes_polled_21=total_votes_GEN+total_votes_SC+total_votes_ST
                category=["TOATL VOTES POLLED TN 21","GEN","SC","ST"]
                votes=[total_votes_polled_21, total_votes_GEN,total_votes_SC,total_votes_ST]
                total_votes = pd.DataFrame({"category": category, "votes": votes})
                trans=total_votes.transpose()
                st.write(trans)
                fig = px.pie(total_votes, values='votes', names='category')
                st.plotly_chart(fig)
                
    def rejected_votes():
        total = dataset1_cleaned.loc['votes rejected'].sum()
        gen = dataset1_cleaned.loc['votes rejected', 'GEN']
        sc = dataset1_cleaned.loc['votes rejected', 'SC']
        st_ = dataset1_cleaned.loc['votes rejected', 'ST']  # Renamed to avoid shadowing the `st` import
        category = ["TOTAL VOTES REJECTED", "GEN", "SC", "ST"]
        votes = [total, gen, sc, st_]
        total_votes = pd.DataFrame({"category": category, "votes": votes})
        st.write(total_votes)
        fig = px.pie(total_votes, values='votes', names='category')
        st.plotly_chart(fig)
    def valid_votes():
        total = dataset1_cleaned.loc['valid votes'].sum()
        gen = dataset1_cleaned.loc['valid votes', 'GEN']
        sc = dataset1_cleaned.loc['valid votes', 'SC']
        st_ = dataset1_cleaned.loc['valid votes', 'ST']  # Renamed to avoid shadowing the `st` import
        category = ["TOTAL VALID VOTES", "GEN", "SC", "ST"]
        votes = [total, gen, sc, st_]
        total_votes = pd.DataFrame({"category": category, "votes": votes})
        trans = total_votes.transpose()
        st.write(trans)
        fig = px.pie(total_votes, values='votes', names='category')
        st.plotly_chart(fig)
    def overall():
        voters=dataset1_cleaned.loc['TOTAL voters'].sum()
        total_votes_GEN = (dataset1_cleaned.loc['voted MALE']['GEN'] +dataset1_cleaned.loc['voted FEMALE']['GEN'] +dataset1_cleaned.loc['voted THIRD GENDER']['GEN'] +dataset1_cleaned.loc['POSTAL votes']['GEN'] +dataset1_cleaned.loc['NOTA VOTES']['GEN'])
        total_votes_SC = (dataset1_cleaned.loc['voted MALE']['SC'] +dataset1_cleaned.loc['voted FEMALE']['SC'] + dataset1_cleaned.loc['voted THIRD GENDER']['SC'] + dataset1_cleaned.loc['POSTAL votes']['SC'] + dataset1_cleaned.loc['NOTA VOTES']['SC'])
        total_votes_ST = (dataset1_cleaned.loc['voted MALE']['ST'] +dataset1_cleaned.loc['voted FEMALE']['ST'] +dataset1_cleaned.loc['voted THIRD GENDER']['ST'] +dataset1_cleaned.loc['POSTAL votes']['ST'] +dataset1_cleaned.loc['NOTA VOTES']['ST'])
        total_votes_polled_21=total_votes_GEN+total_votes_SC+total_votes_ST
        rejected=dataset1_cleaned.loc['votes rejected'].sum()
        valid=dataset1_cleaned.loc['valid votes'].sum()
        data={"Total":["VOTERS","VOTES POLLED","REJECTED VOTES","VALIDVOTES"],
                "votes":[voters,total_votes_polled_21,rejected,valid]}
        df=pd.DataFrame(data)
        st.dataframe(df)
        fig = px.area(df, x='Total', y='votes',color_discrete_sequence=['tomato'])
        st.write(fig)


    if button9:
        st.markdown("<h1 style='color: gray';>Election Outcome Analysis: Total Votes Cast, Rejected Votes, and Valid Votes</h1>", unsafe_allow_html=True)
        st.caption("""Examining the total number of votes cast, rejected votes, and valid votes provides valuable
                            insights into election outcomes and the integrity of the democratic process. By analyzing
                            these metrics, we gain a comprehensive understanding of voter participation, ballot validity
                            and the overall effectiveness of electoral procedures. This exploration aims to shed light on
                            the distribution and significance of votes cast, rejected, and deemed valid, offering valuable
                            perspectives on the health of democracy and the electoral system's performance.""")
        tab1, tab2, tab3,tab4,tab5,tab6= st.tabs(["Total Votes Cast vs Rejected Votes vs and Valid Votes", "Total voters","Total Votes Cast", "Total Rejected Votes","Total valid votes","Overall"])
        with tab1:
            valid_rej_total()
        with tab2:
            total_voters()
        
        with tab3:
                
            toatl_votes()
        with tab4:
                
            rejected_votes()
        with tab5:
            
            valid_votes()
        with tab6:
            overall()







    def overall_electionmetric():
            

            voters=dataset1_cleaned.loc['TOTAL voters'].sum()
            total_votes_GEN = (dataset1_cleaned.loc['voted MALE']['GEN'] +dataset1_cleaned.loc['voted FEMALE']['GEN'] +dataset1_cleaned.loc['voted THIRD GENDER']['GEN'] +dataset1_cleaned.loc['POSTAL votes']['GEN'] +dataset1_cleaned.loc['NOTA VOTES']['GEN'])
            total_votes_SC = (dataset1_cleaned.loc['voted MALE']['SC'] +dataset1_cleaned.loc['voted FEMALE']['SC'] + dataset1_cleaned.loc['voted THIRD GENDER']['SC'] + dataset1_cleaned.loc['POSTAL votes']['SC'] + dataset1_cleaned.loc['NOTA VOTES']['SC'])
            total_votes_ST = (dataset1_cleaned.loc['voted MALE']['ST'] +dataset1_cleaned.loc['voted FEMALE']['ST'] +dataset1_cleaned.loc['voted THIRD GENDER']['ST'] +dataset1_cleaned.loc['POSTAL votes']['ST'] +dataset1_cleaned.loc['NOTA VOTES']['ST'])
            votes=total_votes_GEN+total_votes_SC+total_votes_ST
            rejected_votes=dataset1_cleaned.loc['votes rejected'].sum()
            valid_votes=dataset1_cleaned.loc['valid votes'].sum()
            poll_percentage= dataset1_cleaned.loc['POLL PERCENTAGE'].sum()
            polling_station=dataset1_cleaned.loc['NO. OF POLLING STATIONS'].sum()
            avg_indi_per_polling= dataset1_cleaned.loc['Average no of electors per polling stations'].sum()
            category=["TOTAL VOTERS","TOTAL VOTES CASTS","TOTAL VOTES REJECTED","TOTAL VALID VOTES","TOTAL POLL PERCENTAGE","TOTAL POLLING STATAION","AVERAGE VOTERS PER POLLING STATION"]
            votes=[voters,votes,rejected_votes,valid_votes,poll_percentage,polling_station,avg_indi_per_polling]
            total_votes = pd.DataFrame({"category": category, "votes": votes})
            trans=total_votes.transpose()
            st.write("Electoral Metrics Overview: Insights into Voter Participation and Polling Efficiency")
            st.write(trans)
            fig = px.bar(total_votes, x='category', y='votes',color_discrete_sequence=['DarkOliveGreen'],title="Voter Engagement Spectrum: Analyzing Participation and Efficiency Trends")
            st.write(fig)
            
    if button10:
        st.markdown("<h1 style='color: gray';>Overall Understanding Voter Participation and Election Efficiency: A Case Study Analysis</h1>", unsafe_allow_html=True)
        st.caption("""Explore the intricate dynamics of voter participation and election efficiency through an in-depth analysis of key metrics.
                            From the total number of voters to the distribution of rejected and valid votes, delve into the nuances shaping electoral
                            processes. This study unveils insights into poll percentage trends, shedding light on the democratic engagement within the
                            electorate. Additionally, examining the correlation between the number of polling stations and the average voter turnout per
                            station offers valuable perspectives on accessibility and logistical challenges. Join us as we dissect the data to glean valuable
                            insights into the dynamics of democracy in action.""")
        overall_electionmetric()





    
        

