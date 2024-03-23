from requests import get
import pandas as pd
import openpyxl
import os
import webbrowser
import streamlit as st
import plotly.express as px
import time
from pandasai import SmartDataframe
from pandasai.llm import OpenAI 
import os
st.set_page_config(
    page_title="Election Analytics Hub!",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
   
)
pd.options.display.max_rows = 300
pd.options.display.max_columns = 8
url1 = "https://github.com/mydeenraahina/data_set/raw/main/candidatesdetails.xlsx"
file_1 = "candidatesdetails.xlsx"


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
dataset7 = Read_Data.Read_Excel(url1,file_1)

class Clean_Dataset7:
    
    def removing_duplicates(self, dataset):
        # Removing duplicate values
        dataset.drop_duplicates(inplace=True)
        
    def droping_cols(self, dataset):
        # List of columns dropped from the DataFrame
        drop_columns = ["GENERAL","POSTAL","TOTAL","% VOTES POLLED","TOTAL ELECTORS"]
        # Drop the specified columns
        dataset.drop(columns=drop_columns, inplace=True)
        
    def setting_index(self, dataset):
        # Set 'PARTIES' column as the index
        dataset.set_index('AC NAME', inplace=True)

    def remove_none_values(self, dataset):
        # Remove rows containing None values
        dataset.dropna(inplace=True)
        return dataset

    def cleaned_data(self, dataframe):
        # Create a copy to avoid modifying the original DataFrame
        dataset = dataframe.copy()

        # Apply cleaning steps
        self.removing_duplicates(dataset)
        self.droping_cols(dataset)
        self.setting_index(dataset)
        dataset = self.remove_none_values(dataset)

        # Return the cleaned dataset
        return dataset


cleaned_dataset7 = Clean_Dataset7()
dataset7_cleaned = cleaned_dataset7.cleaned_data(dataset7)

st.markdown("<h1 style='color: #ff0066' ;> Demographic Analysis: Tamil Nadu Election Candidates!</h1>", unsafe_allow_html=True)
st.write("Discover Detailed Insights and Nomination Metrics in the Election")
col1,col2=st.columns(2)
with col1:
    st.title(" Get Started!")
    st.write("🗳️ Uncover Election Nomination Insights. Click on the Metrics Below to Dive into the Analysis!")

    
    

   


with col2:
    st.image("picture1.png",width=200) 





# Define buttons with numbering, icons, and explanatory text
with st.expander("🔍 Explore different aspects of the Tamil Nadu 2021 📈 election"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("🎯 Tamil Nadu Election: Understanding Total Candidates", unsafe_allow_html=True)
        button1 = st.button("Click to View", key="button1", type="primary")
        st.markdown("🎯 Age Group Candidates Analysis", unsafe_allow_html=True)
        button2 = st.button("Click to View", key="button2", type="primary")
        
    if button1:
        def total_can_gen_wise():
            total_candidates = len(dataset7_cleaned["CANDIDATE NAME"])
            total_male = 0
            total_female = 0
            total_third = 0

            for candidate_name in dataset7_cleaned["CANDIDATE NAME"]:
                if dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "SEX"].iloc[0] == "MALE":
                    total_male += 1
                elif dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "SEX"].iloc[0] == "FEMALE":
                    total_female += 1
                else:
                    total_third += 1

            category = ["TOTAL CANDIDATES TN 21", "TOTAL MALE CANDIDATES", "TOTAL FEMALE CANDIDATES", "TOTAL THIRD GENDER CANDIDATES"]
            candidates = [total_candidates, total_male, total_female, total_third]

            df = pd.DataFrame({"category": category, "no.of candidates": candidates})
            st.write(df)
        

            fig = px.bar(df, x="category", y="no.of candidates",color_discrete_sequence=["violet"])
            st.write(fig)
        
        def male_candidate():
            total_male = 0
            total_male_sc = 0
            total_male_st = 0
            total_male_general = 0
            total_candidates_tn = len(dataset7_cleaned)

            for candidate_name in dataset7_cleaned["CANDIDATE NAME"]:
                sex = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "SEX"].iloc[0]
                category = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "CATEGORY"].iloc[0]

                if sex == "MALE":
                    total_male += 1
                    if category == "SC":
                        total_male_sc += 1
                    elif category == "ST":
                        total_male_st += 1
                    elif category == "GENERAL":
                        total_male_general += 1

            category = ["TOTAL CANDIDATES TN", "TOTAL MALE CANDIDATES","TOTAL MALE GENERAL CANDIDATES", "TOTAL MALE SC CANDIDATES", "TOTAL MALE ST CANDIDATES"]
            candidates = [total_candidates_tn, total_male , total_male_general, total_male_sc, total_male_st]

            df = pd.DataFrame({"category": category, "no.of candidates": candidates})
            st.write(df)
            fig = px.bar(df, x="category", y="no.of candidates",color_discrete_sequence=["black"])
            st.write(fig)

            

        def female_candidate():
            total_female = 0
            total_female_sc = 0
            total_female_st = 0
            total_female_general = 0
            total_candidates_tn = len(dataset7_cleaned)

            for candidate_name in dataset7_cleaned["CANDIDATE NAME"]:
                sex = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "SEX"].iloc[0]
                category = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "CATEGORY"].iloc[0]

                if sex == "FEMALE":
                    total_female += 1
                    if category == "SC":
                        total_female_sc += 1
                    elif category == "ST":
                        total_female_st += 1
                    elif category == "GENERAL":
                        total_female_general += 1

            category = ["TOTAL CANDIDATES TN", "TOTAL FEMALE CANDIDATES", "TOTAL FEMALE GENERAL CANDIDATES","TOTAL FEMALE SC CANDIDATES", "TOTAL FEMALE ST CANDIDATES"]
            candidates = [total_candidates_tn, total_female, total_female_general, total_female_sc, total_female_st]

            df = pd.DataFrame({"category": category, "no.of candidates": candidates})
            st.write(df)
            fig = px.bar(df, x="category", y="no.of candidates",color_discrete_sequence=["green"])
            st.write(fig)
        def third_candidate():
            total_third = 0
            total_third_sc = 0
            total_third_st = 0
            total_third_general = 0
            total_candidates_tn = len(dataset7_cleaned)

            for candidate_name in dataset7_cleaned["CANDIDATE NAME"]:
                sex = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "SEX"].iloc[0]
                category = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "CATEGORY"].iloc[0]

                if sex == "THIRD":
                    total_third += 1
                    if category == "SC":
                        total_third_sc += 1
                    elif category == "ST":
                        total_third_st += 1
                    elif category == "GENERAL":
                        total_third_general += 1

            category = ["TOTAL CANDIDATES TN", "TOTAL THIRD CANDIDATES","TOTAL THIRD GENERAL CANDIDATES", "TOTAL THIRD SC CANDIDATES", "TOTAL THIRD ST CANDIDATES"]
            candidates = [total_candidates_tn, total_third, total_third_general,total_third_sc, total_third_st]

            df = pd.DataFrame({"category": category, "no.of candidates": candidates})
            st.write(df)
            fig = px.bar(df, x="category", y="no.of candidates",color_discrete_sequence=["indianred"])
            st.write(fig)

        def total_cat_candidate():
            total_candidates = len(dataset7_cleaned["CANDIDATE NAME"])
            total_sc = 0
            total_st = 0
            total_general = 0

            for candidate_name in dataset7_cleaned["CANDIDATE NAME"]:
                category = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "CATEGORY"].iloc[0]

                if category == "SC":
                    total_sc += 1
                elif category == "ST":
                    total_st += 1
                else:
                    total_general += 1

            category = ["TOTAL CANDIDATES TN 21", "TOTAL GENERAL CANDIDATES", "TOTAL SC CANDIDATES", "TOTAL ST CANDIDATES"]
            candidates = [total_candidates, total_general, total_sc, total_st]

            df = pd.DataFrame({"category": category, "no.of candidates": candidates})
            st.write(df)

            fig = px.bar(df, x="category", y="no.of candidates",color_discrete_sequence=["cyan"])
            st.write(fig)
            
        def gen_category_candidates():
            total_candidates = len(dataset7_cleaned["CANDIDATE NAME"])
            total_general_male = 0
            total_general_female = 0
            total_general_third = 0

            for candidate_name in dataset7_cleaned["CANDIDATE NAME"]:
                sex = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "SEX"].iloc[0]
                category = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "CATEGORY"].iloc[0]

                if category == "GENERAL":
                    if sex == "MALE":
                        total_general_male += 1
                    elif sex == "FEMALE":
                        total_general_female += 1
                    else:
                        total_general_third += 1

            category = ["TOTAL CANDIDATES TN 2021","TOTAL GENERAL MALE", "TOTAL GENERAL FEMALE", "TOTAL GENERAL THIRD"]
            candidates = [total_candidates ,total_general_male, total_general_female, total_general_third]

            df = pd.DataFrame({"category": category, "no.of candidates": candidates})
            st.write(df)
            fig=px.bar(df,x="category",y="no.of candidates",color_discrete_sequence=["tomato"])
            st.write(fig)


        def sc_category_candidates():
            total_candidates = len(dataset7_cleaned["CANDIDATE NAME"])
            total_sc_male = 0
            total_sc_female = 0
            total_sc_third = 0

            for candidate_name in dataset7_cleaned["CANDIDATE NAME"]:
                sex = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "SEX"].iloc[0]
                category = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "CATEGORY"].iloc[0]

                if category == "SC":
                    if sex == "MALE":
                        total_sc_male += 1
                    elif sex == "FEMALE":
                        total_sc_female += 1
                    else:
                        total_sc_third += 1

            category = ["TOTAL CANDIDATES TN 2021","TOTAL SC MALE", "TOTAL SC FEMALE", "TOTAL SC THIRD"]
            candidates = [total_candidates ,total_sc_male, total_sc_female, total_sc_third]

            df = pd.DataFrame({"category": category, "no.of candidates": candidates})
            st.write(df)
            fig=px.bar(df,x="category",y="no.of candidates")
            st.write(fig)

        def st_category_candidates():
            total_candidates = len(dataset7_cleaned["CANDIDATE NAME"])
            total_st_male = 0
            total_st_female = 0
            total_st_third = 0

            for candidate_name in dataset7_cleaned["CANDIDATE NAME"]:
                sex = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "SEX"].iloc[0]
                category = dataset7_cleaned.loc[dataset7_cleaned["CANDIDATE NAME"] == candidate_name, "CATEGORY"].iloc[0]

                if category == "ST":
                    if sex == "MALE":
                        total_st_male += 1
                    elif sex == "FEMALE":
                        total_st_female += 1
                    else:
                        total_st_third += 1

            category = ["TOTAL CANDIDATES TN 2021","TOTAL ST MALE", "TOTAL ST FEMALE", "TOTAL ST THIRD"]
            candidates = [total_candidates ,total_st_male, total_st_female, total_st_third]

            df = pd.DataFrame({"category": category, "no.of candidates": candidates})
            st.write(df)
            fig=px.bar(df,x="category",y="no.of candidates")
            st.write(fig)
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8= st.tabs(["Total Candidates", "Male Candidates", "Female Candidates", "Third Gender Candidates", "Total Caste Category Candidates", "General Category Candidates", "SC Category Candidates", "ST Category Candidates"])

        with tab1:
            total_can_gen_wise()
        with tab2:
            male_candidate()
        with tab3:
            female_candidate()
        with tab4:
            third_candidate()
        with tab5:
            total_cat_candidate()
        with tab6:
            gen_category_candidates()
        with tab7:
            sc_category_candidates()
        with tab8:
            st_category_candidates()



with col2:

    # Define function for total candidates gender-wise
    def total_can_gen_wise(constituency_data, constituency_name):
        # Total Candidates
        total_candidates = len(constituency_data)

        # Male Candidates
        male_candidates = constituency_data[constituency_data["SEX"] == "MALE"]
        total_male = len(male_candidates)

        # Female Candidates
        female_candidates = constituency_data[constituency_data["SEX"] == "FEMALE"]
        total_female = len(female_candidates)

        # Transgender Candidates
        trans_candidates = constituency_data[constituency_data["SEX"] == "TRANS"]
        total_trans = len(trans_candidates)

        category = [f"TOTAL CANDIDATES IN {constituency_name}", f"TOTAL MALE CANDIDATES IN {constituency_name}",
                    f"TOTAL FEMALE CANDIDATES IN {constituency_name}", f"TOTAL THIRD GENDER CANDIDATES IN {constituency_name}"]
        candidates = [total_candidates, total_male, total_female, total_trans]
        df = pd.DataFrame({"category": category, "candidates": candidates})
        st.write(df)
        fig = px.bar(df, x="category", y="candidates")
        st.write(fig)

# Define function for male candidates gender-wise
# Define function for male candidates gender-wise
    def male_candidate(constituency_data, constituency_name):
        # Male Candidates by Category
        male_general = len(constituency_data[(constituency_data["SEX"] == "MALE") & (constituency_data["CATEGORY"] == "GENERAL")])
        male_sc = len(constituency_data[(constituency_data["SEX"] == "MALE") & (constituency_data["CATEGORY"] == "SC")])
        male_st = len(constituency_data[(constituency_data["SEX"] == "MALE") & (constituency_data["CATEGORY"] == "ST")])

        category = [f"TOTAL CANDIDATES IN {constituency_name}", f"TOTAL MALE GENERAL CANDIDATES IN {constituency_name}",
                    f"TOTAL MALE SC CANDIDATES IN {constituency_name}", f"TOTAL MALE ST CANDIDATES IN {constituency_name}"]
        candidates = [len(constituency_data)] + [male_general, male_sc, male_st]
        df = pd.DataFrame({"category": category, "candidates": candidates})
        st.write(df)
        fig = px.bar(df, x="category", y="candidates")
        st.write(fig)


# Define function for female candidates gender-wise
    def female_candidate(constituency_data, constituency_name):
        # Female Candidates by Category
        female_general = len(constituency_data[(constituency_data["SEX"] == "FEMALE") & (constituency_data["CATEGORY"] == "GENERAL")])
        female_sc = len(constituency_data[(constituency_data["SEX"] == "FEMALE") & (constituency_data["CATEGORY"] == "SC")])
        female_st = len(constituency_data[(constituency_data["SEX"] == "FEMALE") & (constituency_data["CATEGORY"] == "ST")])

        category = [f"TOTAL CANDIDATES IN {constituency_name}", f"TOTAL FEMALE GENERAL CANDIDATES IN {constituency_name}",
                    f"TOTAL FEMALE SC CANDIDATES IN {constituency_name}", f"TOTAL FEMALE ST CANDIDATES IN {constituency_name}"]
        candidates =  [len(constituency_data)] + [female_general, female_sc, female_st]
        df = pd.DataFrame({"category": category, "candidates": candidates})
        st.write(df)
        fig = px.bar(df, x="category", y="candidates")
        st.write(fig)


    def third_candidate(constituency_data, constituency_name):
        # Transgender Candidates by Category
        trans_general = len(constituency_data[(constituency_data["SEX"] == "TRANS") & (constituency_data["CATEGORY"] == "GENERAL")])
        trans_sc = len(constituency_data[(constituency_data["SEX"] == "TRANS") & (constituency_data["CATEGORY"] == "SC")])
        trans_st = len(constituency_data[(constituency_data["SEX"] == "TRANS") & (constituency_data["CATEGORY"] == "ST")])

        category = [f"TOTAL CANDIDATES IN {constituency_name}",
                    f"TOTAL THIRD GENDERS GENERAL CANDIDATES IN {constituency_name}",
                    f"TOTAL THIRD GENDERS SC CANDIDATES IN {constituency_name}",
                    f"TOTAL THIRD GENDER ST CANDIDATES IN {constituency_name}"]
        candidates = [len(constituency_data)] + [trans_general, trans_sc, trans_st]
        df = pd.DataFrame({"category": category, "candidates": candidates})
        st.write(df)
        fig = px.bar(df, x="category", y="candidates")
        st.write(fig)
        st.write(f"---")


    # Define function for total candidates by category
    def total_cat_candidate(constituency_data):
        # Total Candidates by Category
        total_general = len(constituency_data[constituency_data["CATEGORY"] == "GENERAL"])
        total_sc = len(constituency_data[constituency_data["CATEGORY"] == "SC"])
        total_st = len(constituency_data[constituency_data["CATEGORY"] == "ST"])

        total_category_df = pd.DataFrame({
            "Category": ["TOTAL GENERAL CANDIDATES", "TOTAL SC CANDIDATES", "TOTAL ST CANDIDATES"],
            "Total Candidates": [total_general, total_sc, total_st]
        })
        st.write(total_category_df)
        fig = px.bar(total_category_df, x="Category", y="Total Candidates")
        st.write(fig)

    # Define function for general category candidates
    def gen_category_candidates(constituency_data):
        # General Category Candidates by Gender
        gen_candidates = constituency_data[constituency_data["CATEGORY"] == "GENERAL"]
        male_gen = len(gen_candidates[gen_candidates["SEX"] == "MALE"])
        female_gen = len(gen_candidates[gen_candidates["SEX"] == "FEMALE"])
        trans_gen = len(gen_candidates[gen_candidates["SEX"] == "TRANS"])

        gen_gender_df = pd.DataFrame({
            "Gender": ["TOTAL Male CANDIDATES", "TOTAL Female CANDIDATES", "TOTAL Transgender CANDIDATES"],
            "Total GENERAL Candidates": [male_gen, female_gen, trans_gen]
        })
        st.write(gen_gender_df)
        fig = px.bar(gen_gender_df, x="Gender", y="Total GENERAL Candidates")
        st.write(fig)

    # Define function for SC category candidates
    def sc_category_candidates(constituency_data):
        # SC Category Candidates by Gender
        sc_candidates = constituency_data[constituency_data["CATEGORY"] == "SC"]
        male_sc = len(sc_candidates[sc_candidates["SEX"] == "MALE"])
        female_sc = len(sc_candidates[sc_candidates["SEX"] == "FEMALE"])
        trans_sc = len(sc_candidates[sc_candidates["SEX"] == "TRANS"])

        sc_gender_df = pd.DataFrame({
            "Gender": ["TOTAL Male CANDIDATES", "TOTAL Female CANDIDATES", "TOTAL Transgender CANDIDATES"],
            "Total SC Candidates": [male_sc, female_sc, trans_sc]
        })
        st.write(sc_gender_df)
        fig = px.bar(sc_gender_df, x="Gender", y="Total SC Candidates")
        st.write(fig)

    # Define function for ST category candidates
    def st_category_candidates(constituency_data):
        # ST Category Candidates by Gender
        st_candidates = constituency_data[constituency_data["CATEGORY"] == "ST"]
        male_st = len(st_candidates[st_candidates["SEX"] == "MALE"])
        female_st = len(st_candidates[st_candidates["SEX"] == "FEMALE"])
        trans_st = len(st_candidates[st_candidates["SEX"] == "TRANS"])

        st_gender_df = pd.DataFrame({
            "Gender": ["TOTAL Male CANDIDATES", "TOTAL Female CANDIDATES", "TOTAL Transgender CANDIDATES"],
            "Total ST Candidates": [male_st, female_st, trans_st]
        })
        st.write(st_gender_df)
        fig = px.bar(st_gender_df, x="Gender", y="Total ST Candidates")
        st.write(fig)


    constituency_names = dataset7_cleaned.index.unique()

    st.write("🎯Total Candidates Across Constituencies")
    selected_constituencies = st.multiselect("Select Constituencies", constituency_names)


    for constituency_name in selected_constituencies:
        constituency_data = dataset7_cleaned.loc[constituency_name]


        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8= st.tabs(["Total Candidates", "Male Candidates", "Female Candidates", "Third Gender Candidates", "Total Caste Category Candidates", "General Category Candidates", "SC Category Candidates", "ST Category Candidates"])

        with tab1:
            total_can_gen_wise(constituency_data, constituency_name)
        with tab2:
            male_candidate(constituency_data, constituency_name)
        with tab3:
            female_candidate(constituency_data, constituency_name)
        with tab4:
            third_candidate(constituency_data, constituency_name)
        with tab5:
            total_cat_candidate(constituency_data)
        with tab6:
            gen_category_candidates(constituency_data)
        with tab7:
            sc_category_candidates(constituency_data)
        with tab8:
            st_category_candidates(constituency_data)
        
    

    if button2:
        total_candidates = len(dataset7_cleaned)

        between_25_35 = 0
        between_36_45 = 0
        between_46_55 = 0
        between_56_65 = 0
        between_66_80 = 0

        for age in dataset7_cleaned["AGE"]:
            if 25 <= age <= 35:
                between_25_35 += 1
            elif 36 <= age <= 45:
                between_36_45 += 1
            elif 46 <= age <= 55:
                between_46_55 += 1
            elif 56 <= age <= 65:
                between_56_65 += 1
            elif 66 <= age <= 80:
                between_66_80 += 1
        def age_grp_candiadtes_genwise_tn():
            total_candidates=len(dataset7_cleaned["CANDIDATE NAME"])
            age_groups = ["TOTAL CANDIDATES","25-35", "36-45", "46-55", "56-65", "66-80"]
            counts = [total_candidates,between_25_35, between_36_45, between_46_55, between_56_65, between_66_80]
            df_age_groups = pd.DataFrame({"Age Group": age_groups, "Candidates Count": counts})

            st.write(df_age_groups)

            fig = px.bar(df_age_groups, x="Age Group",y="Candidates Count", 
                        title="Age Group Distribution of Candidates All Over Tamilnadu")
            st.write(fig)


        def age_grp_candidates_tn_male(dataset7_cleaned):
            total_candidates=len(dataset7_cleaned["CANDIDATE NAME"])

            # Initialize variables for age group counts
            between_25_35 = 0
            between_36_45 = 0
            between_46_55 = 0
            between_56_65 = 0
            between_66_80 = 0

            # Iterate through the age data and count male candidates in each age group
            for age, sex in zip(dataset7_cleaned["AGE"], dataset7_cleaned["SEX"]):
                if sex == "MALE":
                    if 25 <= age <= 35:
                        between_25_35 += 1
                    elif 36 <= age <= 45:
                        between_36_45 += 1
                    elif 46 <= age <= 55:
                        between_46_55 += 1
                    elif 56 <= age <= 65:
                        between_56_65 += 1
                    elif 66 <= age <= 80:
                        between_66_80 += 1

            # Create a DataFrame with age group counts for male candidates
            age_groups = ["TOTAL CANDIDATES","25-35", "36-45", "46-55", "56-65", "66-80"]
            counts = [total_candidates,between_25_35, between_36_45, between_46_55, between_56_65, between_66_80]
            df_age_groups = pd.DataFrame({"Age Group": age_groups, "Male Candidates Count": counts})

            # Display the DataFrame
            st.write(df_age_groups)

            # Create a pie chart using Plotly Express
            fig = px.bar(df_age_groups, x="Age Group", y="Male Candidates Count",
                        title="Age Group Distribution of Male Candidates All Over Tamil Nadu")
            st.plotly_chart(fig)


        def age_grp_candidates_tn_female(dataset7_cleaned):
            total_candidates=len(dataset7_cleaned["CANDIDATE NAME"])

            # Initialize variables for age group counts
            between_25_35 = 0
            between_36_45 = 0
            between_46_55 = 0
            between_56_65 = 0
            between_66_80 = 0

            # Iterate through the age data and count male candidates in each age group
            for age, sex in zip(dataset7_cleaned["AGE"], dataset7_cleaned["SEX"]):
                if sex == "FEMALE":
                    if 25 <= age <= 35:
                        between_25_35 += 1
                    elif 36 <= age <= 45:
                        between_36_45 += 1
                    elif 46 <= age <= 55:
                        between_46_55 += 1
                    elif 56 <= age <= 65:
                        between_56_65 += 1
                    elif 66 <= age <= 80:
                        between_66_80 += 1

            # Create a DataFrame with age group counts for male candidates
            age_groups = ["TOTAL CANDIDATES","25-35", "36-45", "46-55", "56-65", "66-80"]
            counts = [total_candidates,between_25_35, between_36_45, between_46_55, between_56_65, between_66_80]
            df_age_groups = pd.DataFrame({"Age Group": age_groups, "Female Candidates Count": counts})

            # Display the DataFrame
            st.write(df_age_groups)

            # Create a pie chart using Plotly Express
            fig = px.bar(df_age_groups, x="Age Group", y="Female Candidates Count",
                        title="Age Group Distribution of Female Candidates All Over Tamil Nadu")
            st.plotly_chart(fig)



        def age_grp_candidates_tn_trans(dataset7_cleaned):
            total_candidates=len(dataset7_cleaned["CANDIDATE NAME"])

            # Initialize variables for age group counts
            between_25_35 = 0
            between_36_45 = 0
            between_46_55 = 0
            between_56_65 = 0
            between_66_80 = 0

            # Iterate through the age data and count male candidates in each age group
            for age, sex in zip(dataset7_cleaned["AGE"], dataset7_cleaned["SEX"]):
                if sex == "THIRD":
                    if 25 <= age <= 35:
                        between_25_35 += 1
                    elif 36 <= age <= 45:
                        between_36_45 += 1
                    elif 46 <= age <= 55:
                        between_46_55 += 1
                    elif 56 <= age <= 65:
                        between_56_65 += 1
                    elif 66 <= age <= 80:
                        between_66_80 += 1

            # Create a DataFrame with age group counts for male candidates
            age_groups = ["TOTAL CANDIDATES","25-35", "36-45", "46-55", "56-65", "66-80"]
            counts = [total_candidates,between_25_35, between_36_45, between_46_55, between_56_65, between_66_80]
            df_age_groups = pd.DataFrame({"Age Group": age_groups, "trans Candidates Count": counts})

            # Display the DataFrame
            st.write(df_age_groups)

            # Create a pie chart using Plotly Express
            fig = px.bar(df_age_groups, x="Age Group", y="trans Candidates Count",
                        title="Age Group Distribution of Transgender  Candidates All Over Tamil Nadu")
            st.plotly_chart(fig)


        def age_grp_candiadtes_categorywise_tn():
            male_gen_between_36_45 = 0
            female_gen_between_46_55 = 0
            trans_gen_between_56_65 = 0
            between_66_80 = 0





        def age_grp_candidates_tn_gen(dataset7_cleaned):
            total_candidates=len(dataset7_cleaned["CANDIDATE NAME"])
            # Initialize variables for age group counts
            between_25_35 = 0
            between_36_45 = 0
            between_46_55 = 0
            between_56_65 = 0
            between_66_80 = 0

            # Iterate through the age data and count male candidates in each age group
            for age, sex,category in zip(dataset7_cleaned["AGE"], dataset7_cleaned["SEX"],dataset7_cleaned["CATEGORY"]):
                if sex == "MALE" and category=="GENERAL":
                    if 25 <= age <= 35:
                        between_25_35 += 1
                    elif 36 <= age <= 45:
                        between_36_45 += 1
                    elif 46 <= age <= 55:
                        between_46_55 += 1
                    elif 56 <= age <= 65:
                        between_56_65 += 1
                    elif 66 <= age <= 80:
                        between_66_80 += 1

            # Create a DataFrame with age group counts for male candidates
            age_groups = ["TOTAL CANDIDATES","25-35", "36-45", "46-55", "56-65", "66-80"]
            counts = [total_candidates,between_25_35, between_36_45, between_46_55, between_56_65, between_66_80]
            df_age_groups = pd.DataFrame({"Age Group": age_groups, "General category  Candidates Count": counts})

            # Display the DataFrame
            st.write(df_age_groups)

            # Create a pie chart using Plotly Express
            fig = px.bar(df_age_groups, x="Age Group", y="General category  Candidates Count",
                        title="Age Group Distribution of general category Candidates All Over Tamil Nadu")
            st.plotly_chart(fig)
        def age_grp_candidates_tn_sc(dataset7_cleaned):
            total_candidates=len(dataset7_cleaned["CANDIDATE NAME"])
            # Initialize variables for age group counts
            between_25_35 = 0
            between_36_45 = 0
            between_46_55 = 0
            between_56_65 = 0
            between_66_80 = 0

            # Iterate through the age data and count male candidates in each age group
            for age, sex,category in zip(dataset7_cleaned["AGE"], dataset7_cleaned["SEX"],dataset7_cleaned["CATEGORY"]):
                if sex == "MALE" and category=="SC":
                    if 25 <= age <= 35:
                        between_25_35 += 1
                    elif 36 <= age <= 45:
                        between_36_45 += 1
                    elif 46 <= age <= 55:
                        between_46_55 += 1
                    elif 56 <= age <= 65:
                        between_56_65 += 1
                    elif 66 <= age <= 80:
                        between_66_80 += 1

            # Create a DataFrame with age group counts for male candidates
            age_groups = ["TOTAL CANDIDATES","25-35", "36-45", "46-55", "56-65", "66-80"]
            counts = [total_candidates,between_25_35, between_36_45, between_46_55, between_56_65, between_66_80]
            df_age_groups = pd.DataFrame({"Age Group": age_groups, "Sc category  Candidates Count": counts})

            # Display the DataFrame
            st.write(df_age_groups)

            # Create a pie chart using Plotly Express
            fig = px.bar(df_age_groups, x="Age Group", y="Sc category  Candidates Count",
                        title="Age Group Distribution of Sc category Candidates All Over Tamil Nadu")
            st.plotly_chart(fig)
        def age_grp_candidates_tn_st(dataset7_cleaned):
            total_candidates=len(dataset7_cleaned["CANDIDATE NAME"])
            # Initialize variables for age group counts
            between_25_35 = 0
            between_36_45 = 0
            between_46_55 = 0
            between_56_65 = 0
            between_66_80 = 0

            # Iterate through the age data and count male candidates in each age group
            for age, sex,category in zip(dataset7_cleaned["AGE"], dataset7_cleaned["SEX"],dataset7_cleaned["CATEGORY"]):
                if sex == "MALE" and category=="ST":
                    if 25 <= age <= 35:
                        between_25_35 += 1
                    elif 36 <= age <= 45:
                        between_36_45 += 1
                    elif 46 <= age <= 55:
                        between_46_55 += 1
                    elif 56 <= age <= 65:
                        between_56_65 += 1
                    elif 66 <= age <= 80:
                        between_66_80 += 1

            # Create a DataFrame with age group counts for male candidates
            age_groups = ["TOTAL CANDIADATES","25-35", "36-45", "46-55", "56-65", "66-80"]
            counts = [total_candidates,between_25_35, between_36_45, between_46_55, between_56_65, between_66_80]
            df_age_groups = pd.DataFrame({"Age Group": age_groups, "St category  Candidates Count": counts})

            # Display the DataFrame
            st.write(df_age_groups)

            # Create a pie chart using Plotly Express
            fig = px.bar(df_age_groups, x="Age Group", y="St category  Candidates Count",
                        title="Age Group Distribution of St category Candidates All Over Tamil Nadu")
            st.plotly_chart(fig)

        st.write("Age Group Candidates Analysis")
        tab1, tab2, tab3, tab4, tab5, tab6, tab7= st.tabs(["Total Candidates", "Male Candidates", "Female Candidates", "Third Gender Candidates",  "General Category Candidates", "SC Category Candidates", "ST Category Candidates"])

        with tab1:
            age_grp_candiadtes_genwise_tn()
        with tab2:
            age_grp_candidates_tn_male(dataset7_cleaned)
        with tab3:
            age_grp_candidates_tn_female(dataset7_cleaned)
        with tab4:
            age_grp_candidates_tn_trans(dataset7_cleaned)
        with tab5:
            age_grp_candidates_tn_gen(dataset7_cleaned)
        with tab6:
            age_grp_candidates_tn_sc(dataset7_cleaned)
        with tab7:
            age_grp_candidates_tn_st(dataset7_cleaned)
            
        constituency_age_counts = {}
    

    st.write("🎯Analysis of Candidate Demographics and Categories by Party")
    parties_unique = dataset7_cleaned["PARTY"].unique()

    selected_parties = st.multiselect("Select Parties", parties_unique)

    def gender_wise(selected_parties, dataset7_cleaned):
        for party in selected_parties:
            party_candidates = dataset7_cleaned[dataset7_cleaned["PARTY"] == party]
            male_candidates = len(party_candidates[party_candidates["SEX"] == "MALE"])
            female_candidates = len(party_candidates[party_candidates["SEX"] == "FEMALE"])
            trans_candidates = len(party_candidates[party_candidates["SEX"] == "TRANS"])
            
            category = ["TOTAL CANDIDATES", "TOTAL MALE CANDIDATES", "TOTAL FEMALE CANDIDATES", "TOTAL THIRD GENDER CANDIDATES"]
            candidates_count = [len(party_candidates), male_candidates, female_candidates, trans_candidates]
            
            st.write(f"Total number of candidates in {party}:")
            df = pd.DataFrame({"category": category, "candidates_count": candidates_count})
            st.write(df)
            
            fig = px.bar(df, x="category", y="candidates_count", title=f"Total number of candidates in {party}")
            st.plotly_chart(fig)

    def category_wise(selected_parties, dataset7_cleaned):
        for party in selected_parties:
            party_candidates = dataset7_cleaned[dataset7_cleaned["PARTY"] == party]
            gen_candidates = len(party_candidates[party_candidates["CATEGORY"] == "GENERAL"])
            sc_candidates = len(party_candidates[party_candidates["CATEGORY"] == "SC"])
            st_candidates = len(party_candidates[party_candidates["CATEGORY"] == "ST"])
            
            category = ["TOTAL CANDIDATES", "TOTAL GENERAL CANDIDATES", "TOTAL SC CANDIDATES", "TOTAL ST CANDIDATES"]
            candidates_count = [len(party_candidates), gen_candidates, sc_candidates, st_candidates]
            
            st.write(f"Total number of candidates in {party}:")
            df = pd.DataFrame({"category": category, "candidates_count": candidates_count})
            st.write(df)
            
            fig = px.bar(df, x="category", y="candidates_count", title=f"Total number of candidates in {party}")
            st.plotly_chart(fig)

    if selected_parties:
        tab1, tab2 = st.tabs(["Total Candidates genderwise ", "Total Candidates caste category wise"])

        with tab1:
            gender_wise(selected_parties, dataset7_cleaned)
        with tab2:
            category_wise(selected_parties, dataset7_cleaned)

with st.expander("click me to use the Assistant 🤖"):

    conversation_history = []

    # Set OpenAI API key
    os.environ["OPENAI_API_KEY"] = "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"

    # Load DataFramerom Excel file
    path = r"C:\Users\user\AppData\Local\Programs\Python\Python311\Detailed Results.xlsx"
    try:
        df = pd.read_excel(path)
    except Exception as e:
        st.error(f"Error loading Excel file: {e}")



   