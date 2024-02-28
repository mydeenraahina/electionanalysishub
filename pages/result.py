from requests import get
import pandas as pd
import openpyxl
import os
import webbrowser
import streamlit as st
import plotly.express as px
import time

st.set_page_config(
    page_title="Election Analytics Hub!",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
   
)

st.markdown("<h1 style='color: #ff0066' ;> Election Result Insight 2021!</h1>", unsafe_allow_html=True)
st.write("Explore detailed insights in Election Result Taminadu Election 2021!")
col1,col2=st.columns(2)
with col1:
    st.title(" Get Started!")
    st.write("🗳️ Explore insights into Election Result  Click on the metric below to delve into the analysis!")

    
    



with col2:
    st.image("picture1.png",width=200) 



# Instructions for users
st.info("""This  allows you to explore 🗒️ "Election Recap: Comprehensive Analysis of Tamil Nadu 2021 Results
           To get started, expand the section below 👇🏼 and click 🖱️ on the buttons to view specific Details📊.""")








   

url1 = "https://github.com/mydeenraahina/data_set/raw/main/Electors%20Data2.xlsx"
url2 = "https://github.com/mydeenraahina/data_set/raw/main/PoliticalParties_ContestedSeats (4) (3).xlsx"
url3= "https://github.com/mydeenraahina/data_set/raw/main/10-%20Detailed%20Results%20(1).xlsx"
# Local file names to store the downloaded Excel files
file_1 = "Electors%20Data2.xlsx"
file_2 = "PoliticalParties_ContestedSeats (4) (3).xlsx"
file_3="10-%20Detailed%20Results%20(1).xlsx"

class Read_Data():
    # Setting display options for Pandas
    pd.options.display.max_rows = 150
    pd.options.display.max_columns = 8

    @staticmethod
    def Read_Excel(url, file_name):
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
dataset1 = Read_Data.Read_Excel(url1,file_1)
dataset5=Read_Data.Read_Excel(url3,file_3)

class Clean_Dataset1:

    def removing_empty_val(self, dataset):
        # Removing empty values
        dataset.dropna(inplace=True)

    def removing_duplicates(self, dataset):
        # Removing duplicate values
        dataset.drop_duplicates(inplace=True)

    def setting_index(self, dataset):
        # Setting 'Election-related metrics' as the index
        index_name = 'Election-related metrics'
        dataset.set_index(index_name, inplace=True)

    def cleaned_data(self, dataframe):
        # Create a copy to avoid modifying the original DataFrame
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


class Clean_Dataset5:

    
    
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


cleaned_dataset5=Clean_Dataset5()
dataset5_cleaned=cleaned_dataset5.cleaned_data(dataset5)





constituency = dataset5_cleaned.index.unique()

with st.expander("🔍 Explore different aspects of the Tamil Nadu 2021 📈 election"):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h4 style='color: #ff0066' ;> 🎯 Constituency-wise Party Participation and Vote Share Analysis</h4>", unsafe_allow_html=True)

        constituencies = dataset5_cleaned.index.unique().tolist()

        # Generate unique keys for the multiselect widgets
        multiselect_keys = [f"multiselect_{i}" for i in range(len(constituencies))]

        # Multiselect widget to select constituencies
        selected_constituencies = st.multiselect('Select Constituencies', constituencies, key=multiselect_keys[0])

        total_voters=0   
        for i in constituencies:
            
            total_voters+=dataset5_cleaned.loc[i]["TOTAL ELECTORS"].unique()[0]


        def cons_wise_party_and_votes(constituency):
            
            party = dataset5_cleaned.loc[constituency]["PARTY"].tolist()
            total = dataset5_cleaned.loc[constituency]["TOTAL"].tolist()
            party.extend([f"TOTAL VOTES POLLED IN {constituency}", "TOTAL VALID VOTES POLLED TN 21", f"TOTAL VOTERS IN {constituency}","TOTAL VOTERS TN 21"])
            total.extend([ dataset5_cleaned.loc[constituency]["TOTAL"].sum(), dataset1_cleaned.loc["valid votes"].sum(), dataset5_cleaned.loc[constituency]["TOTAL ELECTORS"].unique()[0],total_voters])

            df = pd.DataFrame({"category": party, "votes": total})
            
            # Get candidate names and add them to the DataFrame
            candidate_names = dataset5_cleaned.loc[constituency]["CANDIDATE NAME"].tolist()
            candidate_names.extend([""] * (len(df) - len(candidate_names)))  # Pad the list if necessary
            
            # Concatenate with the existing DataFrame
            df["candidate_name"] = candidate_names
            
            st.write(f"Parties and Candidate Participation & votes Secured by each party and candidate in {constituency}")
            st.write(df)
            fig = px.area(df, x="category", y="votes", title=constituency, color_discrete_sequence=['crimson'])
            st.write(fig)
            
        # Call the function for each selected constituency
        for constituency in selected_constituencies:
            cons_wise_party_and_votes(constituency)

        st.markdown("<h3 style='color: #ff0066' ;> 🎯 Constituency-wise Winner and Runner-up Analysis</h3>", unsafe_allow_html=True)



        def cons_wise_winners(constituency):
            constituency_votes = dataset5_cleaned.loc[constituency]

            total_votes = constituency_votes["TOTAL"].sum()

            winner_votes = constituency_votes["TOTAL"].max()
            runner_up_votes = constituency_votes["TOTAL"][constituency_votes["TOTAL"] < winner_votes].max()
            second_runner_up_votes = constituency_votes["TOTAL"][
                (constituency_votes["TOTAL"] < winner_votes) & (constituency_votes["TOTAL"] < runner_up_votes)
            ].max()

            winner_details = constituency_votes[constituency_votes["TOTAL"] == winner_votes]
            runner_up_details = constituency_votes[constituency_votes["TOTAL"] == runner_up_votes]
            second_runner_up_details = constituency_votes[constituency_votes["TOTAL"] == second_runner_up_votes]

            result_df = pd.concat([winner_details, runner_up_details, second_runner_up_details])

            party_votes_list = result_df[["PARTY", "TOTAL"]].values.tolist()
            candidate_names_list = result_df["CANDIDATE NAME"].values.tolist()

            df = pd.DataFrame(party_votes_list, columns=["Party", "Total Votes"])
            df["Candidate Name"] = candidate_names_list

            status = ["Winner", "Runner-up", "Second Runner-up"]
            df["Status"] = status * (len(df) // len(status)) + status[:len(df) % len(status)]

            total_row = pd.DataFrame([["Total", total_votes, ""]], columns=["Party", "Total Votes", "Status"])

            df = pd.concat([df, total_row], ignore_index=True)
            st.write(df)
            colors = {'Winner': 'green', 'Runner-up': 'orange', 'Second Runner-up': 'blue', 'Total Votes': 'gray'}

            fig = px.bar(df, x='Total Votes', y='Party', orientation='h', title=f'Votes by Party in {constituency}',
                        color='Status', color_discrete_map=colors)

            fig.update_layout(legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ))

            return fig
   
        constituencies = dataset5_cleaned.index.unique().tolist()

        # Generate a unique key for the multiselect widget
        multiselect_key = "constituency_selector"

        selected_constituencies = st.multiselect("Select Constituencies", constituencies, key=multiselect_key)

        if selected_constituencies:
            for constituency in selected_constituencies:
                fig = cons_wise_winners(constituency)
                st.plotly_chart(fig)
        
        pd.options.display.max_rows = 300
        pd.options.display.max_columns = 8

        # Display the time using Streamlit
        # URLs for the Excel files
        path=r'C:\Users\user\AppData\Local\Programs\Python\Python311\10- Detailed Results (1).xlsx'
        dataset6=pd.read_excel(path)
        print(dataset6)
        class Clean_Dataset6:

            
            
            def setting_index(self, dataset):
                dataset.set_index('PARTY', inplace=True)
            def removing_empty_val(self, dataset):
                # Removing empty values
                dataset.dropna(inplace=True)


            def cleaned_data(self, dataframe):
                dataset = dataframe

                
            
                
                self.setting_index(dataset)
                self.removing_empty_val(dataset)
                # Return the cleaned dataset
                return dataset


        cleaned_dataset6=Clean_Dataset6()
        dataset6_cleaned=cleaned_dataset6.cleaned_data(dataset6)
        st.markdown("<h3 style='color: #ff0066' ;>🎯 Tamil Nadu Election Analysis: Party-wise Vote Share</h3>", unsafe_allow_html=True)

        
        total_unique_parties = dataset6_cleaned.index.unique()

        selected_parties = st.multiselect('Select Parties', total_unique_parties)



        for party in selected_parties:
            total_voters = 0
            for constituency in constituencies:
                total_voters += dataset5_cleaned.loc[constituency]["TOTAL ELECTORS"].unique()[0]

            total_votes_polled = dataset6_cleaned["TOTAL"].sum()
            total_valid_votes = dataset1_cleaned.loc["valid votes"].sum()
            cons_party_votes = dataset6_cleaned.loc[party]["TOTAL"].sum()

            categories=["TOATL VOTERS TAMINADU 21","TOTAL VOTES CASTS TAMILNADU 21","TOTAL VALID VOTES TN 21",f"TOTAL VOTES SECURED BY {party}"]
            votes=[total_voters,total_votes_polled,total_valid_votes,cons_party_votes]

            df = pd.DataFrame({"category": categories, "votes": votes})

            st.write(df)
            fig=px.bar(df,x="category",y="votes")
            st.write(fig)

        st.markdown("<h3 style='color: #ff0066' ;>🎯 Party-wise Vote Distribution Across Constituencies</h3>", unsafe_allow_html=True)



        # Assuming 'total_unique_parties' is a list of all unique parties in your dataset
        total_unique_parties = dataset6_cleaned.index.unique().tolist()

        # Generate unique keys for the multiselect widgets
        widget_keys = [f"multiselect_{i}" for i in range(len(total_unique_parties))]

        # Create multiselect widgets with unique keys
        selected_parties = st.multiselect("Select Parties", options=total_unique_parties, key=widget_keys)

        for party in selected_parties:
            total_votes_party = dataset6_cleaned.loc[party]["TOTAL"]
            constituencies = dataset6_cleaned.loc[party]["AC NAME"]
            df = pd.DataFrame({"Constituency": constituencies, "total_votes": total_votes_party})
            st.write(df)
            fig = px.area(df, x="Constituency", y="total_votes")
            st.write(fig)
        
with st.expander("📝Click Me to See Over All Report🏛️"):
    col1, col2 = st.columns(2)
    with col1:


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
            st.markdown("🎯 Comprehensive Overview: Party-wise Vote Shares", unsafe_allow_html=True)
            button1 = st.button("Click to View", key="button1", type="primary")
            if button1:
                parties=[]
                votes_secured=[]
                for party in total_unique_parties:
                    parties.append(party)
                    votes_secured.append(dataset6_cleaned.loc[party]["TOTAL"].sum())
                df=pd.DataFrame({"category":parties,"votes secured":votes_secured})
                st.dataframe(df)
                fig=px.area(df,x="category",y="votes secured")
                st.write(fig)

            st.markdown("🎯Tamil Nadu 2021 Election Recap: Comprehensive Analysis of Winners, Runners-up</h3>", unsafe_allow_html=True)
            button2 = st.button("Click to View", key="button2", type="primary")
            if button2:
                parties = []
                votes_secured = []

                for party in total_unique_parties:
                    parties.append(party)
                    votes_secured.append(dataset6_cleaned.loc[party]["TOTAL"].sum())

                df = pd.DataFrame({"category": parties, "votes secured": votes_secured})

                # Sort the DataFrame by "votes secured" in descending order
                df_sorted = df.sort_values(by="votes secured", ascending=False)

                # Select the top three rows as winner, first runner-up, and second runner-up
                winner_runner_df = df_sorted.head(3)

                # Assigning labels and colors to winner, first runner-up, and second runner-up
                winner_runner_df.loc[:, 'Position'] = ['Winner', 'First Runner-up', 'Second Runner-up']
                winner_runner_df.loc[:, 'Status'] = ['Winner', 'First Runner-up', 'Second Runner-up']

                # Plotting the bar chart
                fig = px.bar(winner_runner_df, x="category", y="votes secured", color='Status',
                            labels={"category": "Party", "votes secured": "Votes Secured"},
                            color_discrete_map={'Winner': 'green', 'First Runner-up': 'blue', 'Second Runner-up': 'yellow'})
                st.plotly_chart(fig)







    

    selected_parties = st.multiselect("Select parties", total_unique_parties)

    for party in selected_parties:
        total_cons = dataset1_cleaned.loc["NO. OF CONSTITUENCIES"].sum()
        total_constituency = len(dataset6_cleaned.loc[party]["AC NAME"])
        constituency = ["TOTAL CONSTITUENCE", "DMK CONSTITUENCE"]
        total = [total_cons, total_constituency]
        df = pd.DataFrame({"constituency": constituency, "Total": total})
        fig = px.bar(df, x="constituency", y="Total")
        st.write(fig)


