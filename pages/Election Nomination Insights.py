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
pd.options.display.max_rows = 300
pd.options.display.max_columns = 8

# Display the time using Streamlit
# URLs for the Excel files
url1 = "https://github.com/mydeenraahina/data_set/raw/main/Candidates%20Data%20Summary.xlsx"

file_1 = "Candidates%20Data%20Summary.xlsx"


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




class Clean_Dataset5:
    def fill_rows(self,dataset):
        dataset['GEN'].fillna(0, inplace=True)
        dataset['SC'].fillna(0, inplace=True)
        dataset['ST'].fillna(0, inplace=True)
    def removing_duplicates(self, dataset):
        # Removing duplicate values
        dataset.drop_duplicates(inplace=True)
    def droping_cols(self, dataset):
        # List of columns dropped from the DataFrame
        drop_columns = ["TOTAL"]
        # Drop the specified columns
        dataset.drop(columns=drop_columns, inplace=True)
    def setting_index(self, dataset):
        # Set 'PARTIES' column as the index
        dataset.set_index('TYPE OF CONSTITUENCY', inplace=True)



    def cleaned_data(self, dataframe):
        # Create a copy to avoid modifying the original DataFrame
        dataset = dataframe

        # Apply cleaning steps
        self.fill_rows(dataset)
        self.droping_cols(dataset)
        self.removing_duplicates(dataset)
        self.setting_index(dataset)
    
        # Return the cleaned dataset
        return dataset


cleaned_dataset5=Clean_Dataset5()
dataset5_cleaned=cleaned_dataset5.cleaned_data(dataset1)
print(dataset5_cleaned)

st.markdown("<h1 style='color: #ff0066' ;> ELECTION NOMINATION INSIGHTS!</h1>", unsafe_allow_html=True)
st.write("Explore detailed insights and  nomination metrics in the election.")
col1,col2=st.columns(2)
with col1:
    st.title(" Get Started!")
    st.write("🗳️ Explore insights into election nominations. Click on the metric below to delve into the analysis!")

    
    

   


with col2:
    st.image("picture1.png",width=200) 



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
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("🎯 Gender and Caste Dynamics in Nomination Submissions", unsafe_allow_html=True)
        button1 = st.button("Click to View", key="button1", type="primary")
        st.markdown("🎯 Gender and Caste Dynamics in Nomination Rejections", unsafe_allow_html=True)
        button2 = st.button("Click to View", key="button2", type="primary")

        st.markdown("🎯 Gender and Caste Dynamics in Nomination Withdraw", unsafe_allow_html=True)
        button3 = st.button("Click to View", key="button3", type="primary")
        st.markdown("🎯 Gender and Caste Dynamics in contested Nomination", unsafe_allow_html=True)
        button4 = st.button("Click to View", key="button4", type="primary")
        

        

    with col2:
        
        st.markdown("🎯 Analysis of Forfeited Deposits in Electoral Candidates 2021", unsafe_allow_html=True)
        button5 = st.button("Click to View", key="button5", type="primary")    

        st.markdown("🎯 Exploring Gender Disparities in Candidate Performance 2021", unsafe_allow_html=True)
        button6 = st.button("Click to View", key="button6", type="primary")

        st.markdown("🎯 Exploring Candidate Performance by Caste Category", unsafe_allow_html=True)
        button7 = st.button("Click to View", key="button7", type="primary")
       


       
def Nomination_Performance_genwise():
    st.header("Exploring Gender Disparities in Candidate Performance: A Comprehensive Analysis of Nomination Submissions, Rejections, Withdrawals, and Contestations")
    st.caption("""Our analysis delves into the performance metrics of candidates based on gender,
                             offering insights into the journey of nominations within electoral processes.
                             The data highlights the number of nominations submitted, rejected, withdrawn,
                             and contested across different genders, shedding light on participation dynamics
                             and challenges faced by male, female, and third-gender candidates.
                             Through visualization and tabulation, we aim to uncover patterns and disparities,
                             contributing to a deeper understanding of candidate engagement in electoral activities.""")


       
def total_performance():
        total_nomation_submitted_males=dataset5_cleaned.loc['(NOMINATION SUBMITTED) MALE'].sum()
        total_nomation_rejected_males=dataset5_cleaned.loc['(NOMINATIONS REJECTED)MALE'].sum()
        total_nomation_withdraw_males=dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)MALE'].sum()
        total_nomation_contested_males=dataset5_cleaned.loc['(CONTESTED CANDIDATES)MALE'].sum()
        total_male_performance=[total_nomation_submitted_males,total_nomation_rejected_males,total_nomation_withdraw_males,total_nomation_contested_males]
        total_nomation_submitted_females=dataset5_cleaned.loc['(NOMINATION SUBMITTED) FEMALE'].sum()
        total_nomation_rejected_females=dataset5_cleaned.loc['(NOMINATIONS REJECTED)FEMALE'].sum()
        total_nomation_withdraw_females=dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)FEMALE'].sum()
        total_nomation_contested_females=dataset5_cleaned.loc['(CONTESTED CANDIDATES)FEMALE'].sum()
        total_female_performance=[total_nomation_submitted_females,total_nomation_rejected_females,total_nomation_withdraw_females,total_nomation_contested_females]
        total_nomation_submitted_thirdgenders=dataset5_cleaned.loc['(NOMINATION SUBMITTED) THIRD GENDER'].sum()
        total_nomation_rejected_thirdgenders=dataset5_cleaned.loc['(NOMINATIONS REJECTED)THIRD GENDER'].sum()
        total_nomation_withdraw_thirdgenders=dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)THIRD GENDER'].sum()
        total_nomation_contested_thirdgenders=dataset5_cleaned.loc['(CONTESTED CANDIDATES)THIRD GENDER'].sum()
        total_thirdgenders_performance=[total_nomation_submitted_thirdgenders,total_nomation_rejected_thirdgenders,total_nomation_withdraw_thirdgenders,total_nomation_contested_thirdgenders]
        gender=["MALE","FEMALE","THIRGENDER","TOTAL"]
        total_per=[sum(total_male_performance),sum(total_female_performance),sum(total_thirdgenders_performance)]
        total=total_per.append(sum(total_per))
        total_nominational_performance=pd.DataFrame({"gender_performance":gender,"Total_no .of performance":total_per})
        trans = total_nominational_performance.transpose()
        st.dataframe(trans)
        fig = px.bar(total_nominational_performance, x='gender_performance', y='Total_no .of performance',color_discrete_sequence=['darkcyan'])
        st.write(fig)

            
        
def performance_male():
        total_nomation_submitted_males=dataset5_cleaned.loc['(NOMINATION SUBMITTED) MALE'].sum()
        total_nomation_rejected_males=dataset5_cleaned.loc['(NOMINATIONS REJECTED)MALE'].sum()
        total_nomation_withdraw_males=dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)MALE'].sum()
        total_nomation_contested_males=dataset5_cleaned.loc['(CONTESTED CANDIDATES)MALE'].sum()
        male_performance=['NOMINATION SUBMITTED','NOMINATIONS REJECTED','NOMINATIONS WITHDRAWNED','CONTESTED CANDIDATES',"TOTAL"]
        total_male_performance=[total_nomation_submitted_males,total_nomation_rejected_males,total_nomation_withdraw_males,total_nomation_contested_males]
        total=total_male_performance.append(sum(total_male_performance))
        total_males_nominational_performance=pd.DataFrame({"performance of male":male_performance,"Total_no .of performance":total_male_performance})
        trans = total_males_nominational_performance.transpose()
        st.dataframe(trans)
        fig = px.pie(total_males_nominational_performance, values='Total_no .of performance', names='performance of male')
        st.write(fig)
 
def performance_female():
        total_nomation_submitted_females=dataset5_cleaned.loc['(NOMINATION SUBMITTED) FEMALE'].sum()
        total_nomation_rejected_females=dataset5_cleaned.loc['(NOMINATIONS REJECTED)FEMALE'].sum()
        total_nomation_withdraw_females=dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)FEMALE'].sum()
        total_nomation_contested_females=dataset5_cleaned.loc['(CONTESTED CANDIDATES)FEMALE'].sum()
        female_performance=['NOMINATION SUBMITTED','NOMINATIONS REJECTED','NOMINATIONS WITHDRAWNED','CONTESTED CANDIDATES',"TOTAL"]
        total_female_performance=[total_nomation_submitted_females,total_nomation_rejected_females,total_nomation_withdraw_females,total_nomation_contested_females]
        total=total_female_performance.append(sum(total_female_performance))
        total_females_nominational_performance=pd.DataFrame({"performance of female":female_performance,"Total_no .of performance":total_female_performance})
        trans = total_females_nominational_performance.transpose()
        st.dataframe(trans)
        fig = px.pie(total_females_nominational_performance, values='Total_no .of performance', names='performance of female')
        st.write(fig)
        
def performance_thirdgen():
        total_nomation_submitted_thirdgenders=dataset5_cleaned.loc['(NOMINATION SUBMITTED) THIRD GENDER'].sum()
        total_nomation_rejected_thirdgenders=dataset5_cleaned.loc['(NOMINATIONS REJECTED)THIRD GENDER'].sum()
        total_nomation_withdraw_thirdgenders=dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)THIRD GENDER'].sum()
        total_nomation_contested_thirdgenders=dataset5_cleaned.loc['(CONTESTED CANDIDATES)THIRD GENDER'].sum()
        thirdgenders_performance=['NOMINATION SUBMITTED','NOMINATIONS REJECTED','NOMINATIONS WITHDRAWNED','CONTESTED CANDIDATES',"TOTAL"]
        total_thirdgenders_performance=[total_nomation_submitted_thirdgenders,total_nomation_rejected_thirdgenders,total_nomation_withdraw_thirdgenders,total_nomation_contested_thirdgenders]
        total=total_thirdgenders_performance.append(sum(total_thirdgenders_performance))
        total_thirdgenders_nominational_performance=pd.DataFrame({"performance of thirdgenders":thirdgenders_performance,"Total_no .of performance":total_thirdgenders_performance})
        trans = total_thirdgenders_nominational_performance.transpose()
        st.dataframe(trans)
        fig = px.pie(total_thirdgenders_nominational_performance, values='Total_no .of performance', names='performance of thirdgenders')
        st.write(fig)
if button6:
    st.header("Exploring Gender Disparities in Candidate Performance: A Comprehensive Analysis of Nomination Submissions, Rejections, Withdrawals, and Contestations")
    st.caption("""Our analysis delves into the performance metrics of candidates based on gender,
                             offering insights into the journey of nominations within electoral processes.
                             The data highlights the number of nominations submitted, rejected, withdrawn,
                             and contested across different genders, shedding light on participation dynamics
                             and challenges faced by male, female, and third-gender candidates.
                             Through visualization and tabulation, we aim to uncover patterns and disparities,
                             contributing to a deeper understanding of candidate engagement in electoral activities.""")


    tab1, tab2, tab3,tab4=st.tabs(["overall performance of candidates in Nomination Tn 21 gender wise","Male Candidate Performance", "Female Candidate Performance", "Third Gender Candidate Performance"])
    with tab1:
       total_performance()
    with tab2:
        performance_male()
    with tab3:
        performance_female()
   
    with tab4:
         performance_thirdgen()

 
def total_per():
    def cateogory(category):
                    category_type = [
                    dataset5_cleaned.loc['(NOMINATION SUBMITTED) MALE'][category],
                    dataset5_cleaned.loc['(NOMINATION SUBMITTED) FEMALE'][category],
                    dataset5_cleaned.loc['(NOMINATION SUBMITTED) THIRD GENDER'][category],  # Use category parameter here
                    dataset5_cleaned.loc['(NOMINATIONS REJECTED)MALE'][category],
                    dataset5_cleaned.loc['(NOMINATIONS REJECTED)FEMALE'][category],
                    dataset5_cleaned.loc['(NOMINATIONS REJECTED)THIRD GENDER'][category],  # Use category parameter here
                    dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)MALE'][category],
                    dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)FEMALE'][category],
                    dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)THIRD GENDER'][category],  # Use category parameter here
                    dataset5_cleaned.loc['(CONTESTED CANDIDATES)MALE'][category],
                    dataset5_cleaned.loc['(CONTESTED CANDIDATES)FEMALE'][category],
                    dataset5_cleaned.loc['(CONTESTED CANDIDATES)THIRD GENDER'][category]  # Use category parameter here
                
                
                
                
                
                ]



                    return sum(category_type)

    category = ["TOTAL PERFORMANCE", "GEN", "SC", "ST"]
    value = [cateogory('GEN'),cateogory('SC'),cateogory('ST')]
    total = sum(value)
    value.insert(0, total)
    total_nominational_performance = pd.DataFrame({"caste category": category, "Total_no .of performance": value})
    trans = total_nominational_performance.transpose()
    st.dataframe(trans)
    fig = px.bar(total_nominational_performance, x='caste category', y='Total_no .of performance', color_discrete_sequence=['forestgreen'])
    st.write(fig)
            
def performance(category):
        total_nomation_submitted=dataset5_cleaned.loc['(NOMINATION SUBMITTED) MALE'][category]
        total_nomation_rejected=dataset5_cleaned.loc['(NOMINATION SUBMITTED) FEMALE'][category]
        total_nomation_withdraw=dataset5_cleaned.loc['(NOMINATION SUBMITTED) THIRD GENDER'][category]
        total_nomation_contested=dataset5_cleaned.loc['(CONTESTED CANDIDATES)MALE'].sum()
        performance=['NOMINATION SUBMITTED','NOMINATIONS REJECTED','NOMINATIONS WITHDRAWNED','CONTESTED CANDIDATES',"TOTAL PERFORMANCE"]
        total_performance=[total_nomation_submitted,total_nomation_rejected,total_nomation_withdraw,total_nomation_contested]
        total=total_performance.append(sum(total_performance))
        total_nominational_performance=pd.DataFrame({"caste category":performance,"Total_no .of performance":total_performance})
        trans = total_nominational_performance.transpose()
        st.dataframe(trans)
        fig = px.pie(total_nominational_performance, values='Total_no .of performance', names='caste category')
        st.write(fig)

if button7:
    st.header("Exploring Candidate Performance by  Caste Category: Nomination Metrics Analysis")
    st.caption("""This analysis delves into the performance metrics of candidates across caste categories (General, Scheduled Caste, Scheduled Tribe).
                            Through visualizations and tabulations, we examine nomination submissions, rejections, withdrawals, and contestations, offering insights
                           into the dynamics of candidate engagement and outcomes within electoral processes.""")


    tab1, tab2, tab3,tab4=st.tabs(["overall performance of candidates in Nomination Tn 21 caste category wise[GEN,SC,ST]","gen category Candidate Performance", "sc category Candidate Performance", "st category Candidate Performance"])
    with tab1:
       total_per()
    with tab2:
        performance('GEN')
    with tab3:
         performance('SC')
   
    with tab4:
          performance('ST')

        
def tot_nomination_sub_gen():
        genders = ["MALE", "FEMALE", "THIRD GENDER"]
        categories = ["TOTAL SUBMISSION","MALE", "FEMALE", "THIRD GENDER"]
        nomination_submitted_by_category_GEN = sum(dataset5_cleaned.loc[f'(NOMINATION SUBMITTED) {gender}']['GEN'] for gender in genders)
        nomination_submitted_by_category_SC = sum(dataset5_cleaned.loc[f'(NOMINATION SUBMITTED) {gender}']['SC'] for gender in genders)
        nomination_submitted_by_category_ST = sum(dataset5_cleaned.loc[f'(NOMINATION SUBMITTED) {gender}']['ST'] for gender in genders)
        nomination_submitted_by_category=[nomination_submitted_by_category_GEN,nomination_submitted_by_category_SC,nomination_submitted_by_category_ST]
        total=nomination_submitted_by_category.insert(0,sum(nomination_submitted_by_category))
        total_nomination_submitted_by_category=pd.DataFrame({"Gender category":categories,"No.of nomination_submitted":nomination_submitted_by_category})
        trans = total_nomination_submitted_by_category.transpose()
        st.dataframe(trans)
        fig = px.area(total_nomination_submitted_by_category, x='Gender category', y='No.of nomination_submitted')
        st.write(fig)
def submission(value):
        nomination_submitted_gen = dataset5_cleaned.loc[value]["GEN"]
        nomination_submitted_sc = dataset5_cleaned.loc[value]["SC"]
        nomination_submitted_st = dataset5_cleaned.loc[value]["ST"]
            
        category = ["TOTAL SUBMISSION", "GEN", "SC", "ST"]
        value = [nomination_submitted_gen, nomination_submitted_sc, nomination_submitted_st]
        total = sum(value)
        value.insert(0, total)

        total_nomination_submitted = pd.DataFrame({"caste Category": category, "No_of_nomination": value})
        trans = total_nomination_submitted.transpose()
        st.dataframe(trans)
        fig = px.line(total_nomination_submitted, x='caste Category', y='No_of_nomination')
        st.write(fig)
def nomination_submitted():
        gen = dataset5_cleaned.loc['(NOMINATION SUBMITTED) MALE']['GEN'] + \
                    dataset5_cleaned.loc['(NOMINATION SUBMITTED) FEMALE']['GEN'] + \
                    dataset5_cleaned.loc['(NOMINATION SUBMITTED) THIRD GENDER']['GEN']
                      
        sc = dataset5_cleaned.loc['(NOMINATION SUBMITTED) MALE']['SC'] + \
                dataset5_cleaned.loc['(NOMINATION SUBMITTED) FEMALE']['SC'] + \
                dataset5_cleaned.loc['(NOMINATION SUBMITTED) THIRD GENDER']['SC']
                     
        st_val = dataset5_cleaned.loc['(NOMINATION SUBMITTED) MALE']['ST'] + \
                 dataset5_cleaned.loc['(NOMINATION SUBMITTED) FEMALE']['ST'] + \
                 dataset5_cleaned.loc['(NOMINATION SUBMITTED) THIRD GENDER']['ST']

        total = gen + sc + st_val
        category = ["TOTAL SUBMISSION","GEN", "SC", "ST"]
        values = [total,gen, sc, st_val]

                # Construct DataFrame
        total_nomination_submitted_by_category = pd.DataFrame({"caste Category": category,
                                                                       "No.of Nomination Submitted": values})

               
        st.write(total_nomination_submitted_by_category)

                # Create plot
        fig = px.area(total_nomination_submitted_by_category, x='caste Category', y='No.of Nomination Submitted', color_discrete_sequence=['cyan'])
                
                # Display plot
        st.plotly_chart(fig)
def nomination_sub_by_each_category(caste):
    nomination_submitted_male = dataset5_cleaned.loc['(NOMINATION SUBMITTED) MALE'][caste]
    nomination_submitted_female= dataset5_cleaned.loc['(NOMINATION SUBMITTED) FEMALE'][caste]
    nomination_submitted_thirdgen = dataset5_cleaned.loc['(NOMINATION SUBMITTED) THIRD GENDER'][caste]
            
    category = ["TOTAL SUBMISSION", "MALE", "FEMALE", "THIRDGENDER"]
    value = [nomination_submitted_male, nomination_submitted_female, nomination_submitted_thirdgen]
    value.insert(0, sum(value))

    total_nomination_submitted = pd.DataFrame({"caste Category": category, "No_of_nomination": value})
    trans = total_nomination_submitted.transpose()
    st.dataframe(trans)
    fig = px.line(total_nomination_submitted, x='caste Category', y='No_of_nomination')
    st.write(fig)
     


            
             
if button1:
    st.header("Exploring the Gender andcaste  Category Dynamics in Nomination Submissions ")
    st.caption("""This analysis delves into the distribution of nomination submissions across different genders and categories,
                            focusing on the representation of various demographic groups in the submission process. By tabulating the
                            total submissions over gender and category (including General, Scheduled Caste, and Scheduled Tribe), as
                             well as displaying the breakdown of submissions for each gender within these categories, we gain insights
                            into the inclusivity and diversity of participation in the nomination process. """)


    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Total no.of nominations submitted by gender-wise",
                                                        "Total nomination submitted males with caste category(2021)",
                                                        "Total nomination submitted females with caste category(2021)",
                                                        "Total nomination submitted thirdgender with caste category(2021)", 
                                                        "Total no.of nominations submitted by each caste category",
                                                        "Total nomination submitted GEN category across gender(2021)", 
                                                        "Total nomination submitted SC category across gender(2021)", 
                                                        "Total nomination submitted ST category across gender(2021)"])
    with tab1:
        tot_nomination_sub_gen()
    with tab2:
        submission('(NOMINATION SUBMITTED) MALE')
    with tab3:
         submission('(NOMINATION SUBMITTED) FEMALE')
    with tab4:
         submission('(NOMINATION SUBMITTED) THIRD GENDER')
    with tab5:
        nomination_submitted()
    with tab6:
        nomination_sub_by_each_category('GEN')
    with tab7:
        nomination_sub_by_each_category("SC")
    with tab8:
        nomination_sub_by_each_category('ST')


def nomi_rejected_category():
         genders = ["MALE", "FEMALE", "THIRD GENDER"]
         categories = ["GEN", "SC", "ST","TOTAL REJECTION"]

         nomination_rejected_by_category_GEN = sum(dataset5_cleaned.loc[f'(NOMINATIONS REJECTED){gender}']['GEN'] for gender in genders)
         nomination_rejected_by_category_SC = sum(dataset5_cleaned.loc[f'(NOMINATIONS REJECTED){gender}']['SC'] for gender in genders)
         nomination_rejected_by_category_ST = sum(dataset5_cleaned.loc[f'(NOMINATIONS REJECTED){gender}']['ST'] for gender in genders)
         nomination_rejected_by_category=[nomination_rejected_by_category_GEN,nomination_rejected_by_category_SC,nomination_rejected_by_category_ST]
         total=nomination_rejected_by_category.append(sum(nomination_rejected_by_category))
         total_nomination_rejected_by_category=pd.DataFrame({"Gender category":categories,"No.of nomination_rejected":nomination_rejected_by_category})
         trans = total_nomination_rejected_by_category.transpose()
         st.dataframe(trans)
         fig = px.area(total_nomination_rejected_by_category, x='Gender category', y='No.of nomination_rejected')
         st.write(fig)
def nom_rejected_genwise():
        male=dataset5_cleaned.loc['(NOMINATIONS REJECTED)MALE'].sum()
        female=dataset5_cleaned.loc['(NOMINATIONS REJECTED)FEMALE'].sum()
        thirdgender=dataset5_cleaned.loc['(NOMINATIONS REJECTED)THIRD GENDER'].sum()
        total=male+female+thirdgender
        category=["TOATL REJECTION","MALE","FEMALE","THIRDGENDER"]
        values=[total,male,female,thirdgender]
        total_nomination_rejected_by_gender=pd.DataFrame({"gender category":category,"No.of nomination_rejected":values})
        trans = total_nomination_rejected_by_gender.transpose()
        st.dataframe(trans)
        fig = px.area(total_nomination_rejected_by_gender, x='gender category', y='No.of nomination_rejected')
        st.write(fig)
def rejection(value):
        nomination_rejection_gen=dataset5_cleaned.loc[value]["GEN"]
        nomination_rejection_sc=dataset5_cleaned.loc[value]["SC"]
        nomination_rejection_st=dataset5_cleaned.loc[value]["ST"]
        category=["TOTAL REJECION  ","GEN","SC","ST"]
        value=[nomination_rejection_gen,nomination_rejection_sc,nomination_rejection_st]
        total=value.insert(0,sum(value))

        total_nomination_rejection=pd.DataFrame({"caste Category":category,"No_of_nomination":value})
        st.dataframe(total_nomination_rejection)
        fig = px.line(total_nomination_rejection, x='caste Category', y='No_of_nomination')
        st.write(fig)
def nomination_rej_by_each_category(caste):
    nomination_rejected_male = dataset5_cleaned.loc['(NOMINATIONS REJECTED)MALE'][caste]
    nomination_rejected_female= dataset5_cleaned.loc['(NOMINATIONS REJECTED)FEMALE'][caste]
    nomination_rejected_thirdgen = dataset5_cleaned.loc['(NOMINATIONS REJECTED)THIRD GENDER'][caste]
            
    category = ["TOTAL SUBMISSION", "MALE", "FEMALE", "THIRDGENDER"]
    value = [nomination_rejected_male, nomination_rejected_female, nomination_rejected_thirdgen]
    value.insert(0, sum(value))

    total_nomination_rejected = pd.DataFrame({"caste Category": category, "No_of_nomination": value})
    trans = total_nomination_rejected.transpose()
    st.dataframe(trans)
    fig = px.line(total_nomination_rejected, x='caste Category', y='No_of_nomination')
    st.write(fig)      

if button2:
    st.header("Examining Gender and caste Category Disparities in Nomination Rejections")
    st.caption("""This analysis delves into the distribution of nomination rejections across different genders and categories,
                        focusing on understanding disparities in the rejection rates among various demographic groups. By tabulating
                         the total rejections over gender and category (including General, Scheduled Caste, and Scheduled Tribe), as
                        well as displaying the breakdown of rejections for each gender within these categories, we gain insights into
                        potential biases or challenges faced by different demographic segments in the nomination process. """)


    tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8=st.tabs(["Total no.of nominations rejected by gender-wise",
                                        "Total nomination  rejected males with caste category(2021)", 
                                        "Total nomination  rejected females with caste category(2021)",
                                        "Total nomination  rejected thirdgender with caste category(2021)",
                                        "Total no.of nominations submitted by each caste category",
                                        "Total nomination rejected GEN category across gender(2021)", 
                                        "Total nomination rejected SC category across gender(2021)", 
                                        "Total nomination rejected ST category across gender(2021)"])
    with tab1:
        nom_rejected_genwise()
    with tab2:
        rejection("(NOMINATIONS REJECTED)MALE")
        
    with tab3:
        rejection('(NOMINATIONS REJECTED)FEMALE')
    with tab4:
        rejection('(NOMINATIONS REJECTED)THIRD GENDER')
    with tab5:
        nomi_rejected_category()
    with tab6:
        nomination_rej_by_each_category('GEN')
    with tab7:
        nomination_rej_by_each_category("SC")
    with tab8:
        nomination_rej_by_each_category('ST')




def nomi_withdraw_cate():
        genders = ["MALE", "FEMALE", "THIRD GENDER"]
        categories = ["GEN", "SC", "ST","TOTAL WITHDRAW"]

        nomination_withdraw_by_category_GEN = sum(dataset5_cleaned.loc[f' (NOMINATIONS WITHDRAWNED){gender}']['GEN'] for gender in genders)
        nomination_withdraw_by_category_SC = sum(dataset5_cleaned.loc[f' (NOMINATIONS WITHDRAWNED){gender}']['SC'] for gender in genders)
        nomination_withdraw_by_category_ST = sum(dataset5_cleaned.loc[f' (NOMINATIONS WITHDRAWNED){gender}']['ST'] for gender in genders)
        nomination_withdraw_by_category=[nomination_withdraw_by_category_GEN,nomination_withdraw_by_category_SC,nomination_withdraw_by_category_ST]
        total=nomination_withdraw_by_category.append(sum(nomination_withdraw_by_category))
        total_nomination_withdraw_by_category=pd.DataFrame({"Gender category":categories,"No.of nomination_withdraw":nomination_withdraw_by_category})
        trans = total_nomination_withdraw_by_category.transpose()
        st.dataframe(trans)
        fig = px.area(total_nomination_withdraw_by_category, x='Gender category', y='No.of nomination_withdraw')
        st.write(fig)
def nomi_withdraw_gen():
        categories=["TOTAL","MALE","FEMALE","THIRDGENDER"]
        male=dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)MALE'].sum()
        female=dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)FEMALE'].sum()
        thirdgender=dataset5_cleaned.loc[' (NOMINATIONS WITHDRAWNED)THIRD GENDER'].sum()
        total=male+female+thirdgender
        value=[total,male,female,thirdgender]
        total_nomination_withdraw_by_gender=pd.DataFrame({"gender category":categories,"No.of nomination_withdraw":value})
        trans = total_nomination_withdraw_by_gender.transpose()
        st.dataframe(trans)
        fig = px.area(total_nomination_withdraw_by_gender, x='gender category', y='No.of nomination_withdraw')
        st.write(fig)
def withdraw(value):
        nomination_withdraw_gen=dataset5_cleaned.loc[value]["GEN"]
        nomination_withdraw_sc=dataset5_cleaned.loc[value]["SC"]
        nomination_withdraw_st=dataset5_cleaned.loc[value]["ST"]
        category=["TOTAL  WITHDRAW","GEN","SC","ST"]
        value=[nomination_withdraw_gen,nomination_withdraw_sc,nomination_withdraw_st]
        total=value.insert(0,sum(value))

        total_nomination_withdraw=pd.DataFrame({"caste Category":category,"No_of_nomination":value})
        trans =total_nomination_withdraw.transpose()
        st.dataframe(trans)
        fig = px.line(total_nomination_withdraw, x='caste Category', y='No_of_nomination')
        st.write(fig)
def nomination_withdraw_by_each_category(caste):
    nomination_withdraw_male = dataset5_cleaned.loc['(NOMINATIONS REJECTED)MALE'][caste]
    nomination_withdraw_female= dataset5_cleaned.loc['(NOMINATIONS REJECTED)FEMALE'][caste]
    nomination_withdraw_thirdgen = dataset5_cleaned.loc['(NOMINATIONS REJECTED)THIRD GENDER'][caste]
            
    category = ["TOTAL SUBMISSION", "MALE", "FEMALE", "THIRDGENDER"]
    value = [nomination_withdraw_male, nomination_withdraw_female, nomination_withdraw_thirdgen]
    value.insert(0, sum(value))

    total_nomination_withdraw= pd.DataFrame({"caste Category": category, "No_of_nomination": value})
    trans = total_nomination_withdraw.transpose()
    st.dataframe(trans)
    fig = px.line(total_nomination_withdraw, x='caste Category', y='No_of_nomination')
    st.write(fig)                
if button3:
    st.header("Exploring Withdrawal Patterns: Gender and caste Category Analysis")
    st.caption("""This analysis investigates the patterns of withdrawal across different genders and categories,
                        shedding light on factors influencing the decision to withdraw nominations. By tabulating the
                         total withdrawals over gender and category (including General, Scheduled Caste, and Scheduled Tribe),
                        and presenting the distribution of withdrawals for each gender within these categories, we gain
                        nsights into the dynamics of participation and engagement in the nomination process.""")


    tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8=st.tabs(["Total no.of nominations withdraw by gender-wise",
                                                       "Total nomination withdraw males with caste category(2021)", 
                                                       "Total nomination withdraw females with caste category(2021)",
                                                       "Total nomination withdraw thirdgender with caste category(2021)",
                                                       "Total no.of nominations withdraw by each caste category",
                                                       "Total nomination withdraw GEN category across gender(2021)", 
                                                        "Total nomination withdraw SC category across gender(2021)", 
                                                        "Total nomination withdraw ST category across gender(2021)"])
    
    with tab1:
        st.write("hello")
        nomi_withdraw_gen()
    with tab2:
        withdraw(' (NOMINATIONS WITHDRAWNED)MALE')
    with tab3:
        withdraw(' (NOMINATIONS WITHDRAWNED)FEMALE')
    with tab4:
        withdraw(' (NOMINATIONS WITHDRAWNED)THIRD GENDER')
    with tab5:
        nomi_withdraw_cate()
    with tab6:
         nomination_withdraw_by_each_category("GEN")
    with tab7:
         nomination_withdraw_by_each_category("SC")
    with tab8:
         nomination_withdraw_by_each_category("ST")

def nomination_contest_genderwise():
        categories=["TOTAL","MALE","FEMALE","THIRDGENDER"]
        male=dataset5_cleaned.loc['(CONTESTED CANDIDATES)MALE'].sum()
        female=dataset5_cleaned.loc['(CONTESTED CANDIDATES)FEMALE'].sum()
        thirdgender=dataset5_cleaned.loc['(CONTESTED CANDIDATES)THIRD GENDER'].sum()
        total=male+female+thirdgender
        value=[total,male,female,thirdgender]
        total_nomination_contest_by_gender=pd.DataFrame({"Gender category":categories,"No.of nomination_withdraw":value})
        trans = total_nomination_contest_by_gender.transpose()
        st.dataframe(trans)
        fig = px.area(total_nomination_contest_by_gender, x='Gender category', y='No.of nomination_withdraw')
        st.write(fig)
def nomation_contest_categwise():
        genders = ["MALE", "FEMALE", "THIRD GENDER"]
        categories = ["TOTAL CONTESTMENT","GEN", "SC", "ST"]


        nomination_contested_by_category_GEN = sum(dataset5_cleaned.loc[f'(CONTESTED CANDIDATES){gender}']['GEN'] for gender in genders)
        nomination_contested_by_category_SC  = sum(dataset5_cleaned.loc[f'(CONTESTED CANDIDATES){gender}']['SC'] for gender in genders)
        nomination_contested_by_category_ST  = sum(dataset5_cleaned.loc[f'(CONTESTED CANDIDATES){gender}']['ST'] for gender in genders)
        nomination_contested_by_category=[nomination_contested_by_category_GEN,nomination_contested_by_category_SC,nomination_contested_by_category_ST]
        toatl=nomination_contested_by_category.insert(0,sum(nomination_contested_by_category))
        total_nomination_contested_by_category=pd.DataFrame({"caste category":categories,"No.of nomination_contested":nomination_contested_by_category})
        trans = total_nomination_contested_by_category.transpose()
        st.dataframe(trans)
        fig = px.area(total_nomination_contested_by_category, x='caste category', y='No.of nomination_contested',color_discrete_sequence=['darkcyan'])
        st.write(fig)
def contest(value):
        nomination_contest_gen=dataset5_cleaned.loc[value]["GEN"]
        nomination_contest_sc=dataset5_cleaned.loc[value]["SC"]
        nomination_contest_st=dataset5_cleaned.loc[value]["ST"]
        category=["TOTAL  CONTESTED","GEN","SC","ST"]
        value=[nomination_contest_gen,nomination_contest_sc,nomination_contest_st]
        total=value.insert(0,sum(value))

        total_nomination_contest=pd.DataFrame({"caste Category":category,"No_of_nomination":value})
        trans =total_nomination_contest.transpose()
        st.dataframe(trans)
        fig = px.line(total_nomination_contest, x='caste Category', y='No_of_nomination')
        st.write(fig)    
def nomination_contest_by_each_category(caste):
    nomination_contest_male = dataset5_cleaned.loc['(NOMINATIONS REJECTED)MALE'][caste]
    nomination_contest_female= dataset5_cleaned.loc['(NOMINATIONS REJECTED)FEMALE'][caste]
    nomination_contest_thirdgen = dataset5_cleaned.loc['(NOMINATIONS REJECTED)THIRD GENDER'][caste]
            
    category = ["TOTAL SUBMISSION", "MALE", "FEMALE", "THIRDGENDER"]
    value = [nomination_contest_male, nomination_contest_female, nomination_contest_thirdgen]
    value.insert(0, sum(value))

    total_nomination_contest= pd.DataFrame({"caste Category": category, "No_of_nomination": value})
    trans = total_nomination_contest.transpose()
    st.dataframe(trans)
    fig = px.line(total_nomination_contest, x='caste Category', y='No_of_nomination')
    st.write(fig)     
if button4:
   st.header("Examining Gender and caste Category Dynamics in Contested Nominations")
   st.caption("""This analysis delves into the distribution of contested nominations across different genders
                        and categories, aiming to understand the representation and engagement of various demographic
                        groups in contested nomination processes. By tabulating the total contested nominations over gender
                        and category (including General, Scheduled Caste, and Scheduled Tribe), and presenting the breakdown
                        of contested nominations for each gender within these categories, we gain insights into the levels of
                        participation and competition among different demographic segments. """)


   tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8=st.tabs(["Total no.of nominations contest by gender-wise",
     "Total nomination contest males with caste category(2021)",
     "Total nomination contest females with caste ategory(2021)",
     "Total nomination contest thirdgender with caste category(2021)",
     "Total no.of nominations contest by each caste category",
     "Total nomination contested GEN category across gender(2021)", 
     "Total nomination contested SC category across gender(2021)", 
     "Total nomination contested ST category across gender(2021)"])
    
   with tab1:
        nomination_contest_genderwise()
   with tab2:
        contest('(CONTESTED CANDIDATES)MALE')
   with tab3:
        contest('(CONTESTED CANDIDATES)FEMALE')
   with tab4:
        contest('(CONTESTED CANDIDATES)THIRD GENDER')
   with tab5:
        nomation_contest_categwise()
   with tab6:
        nomination_contest_by_each_category('GEN')
   with tab7:
        nomination_contest_by_each_category('SC')
   with tab8:
        nomination_contest_by_each_category('ST')
        


def fd_payed_genderwise():
        male=dataset5_cleaned.loc['(FORFEITED DEPOSITS)MALE'].sum()
        female=dataset5_cleaned.loc['(FORFEITED DEPOSITS)FEMALE'].sum()
        thirdgender=dataset5_cleaned.loc['(FORFEITED DEPOSITS)THIRD GENDER'].sum()
        category=["TOTAL","MALE","FEMALE","THIRDGENDER"]
        value=[male,female,thirdgender]
        total=value.insert(0,sum(value))
        total_fd_deposite=pd.DataFrame({"gender category":category,"Total_FD":value})
        trans = total_fd_deposite.transpose()
        st.dataframe(trans)
        fig = px.pie(total_fd_deposite, values='Total_FD', names='gender category')
        st.plotly_chart(fig)
def male():
        gen = dataset5_cleaned.loc['(FORFEITED DEPOSITS)MALE']['GEN']
        sc = dataset5_cleaned.loc['(FORFEITED DEPOSITS)MALE']['SC']
        st_val = dataset5_cleaned.loc['(FORFEITED DEPOSITS)MALE']['ST']
        
        category = ["TOTAL","GEN", "SC", "ST"]
        value = [gen, sc, st_val]
        value.append(sum(value))

        total_male = pd.DataFrame({"caste Category": category, "Total FD": value}) 
        st.write(total_male)
        fig = px.pie(total_male, values='Total FD', names='caste Category', title='Deposit Distribution for Male',
            hole=0.5)  
        st.plotly_chart(fig)
def female():
        gen = dataset5_cleaned.loc['(FORFEITED DEPOSITS)FEMALE']['GEN']
        sc = dataset5_cleaned.loc['(FORFEITED DEPOSITS)FEMALE']['SC']
        st_val = dataset5_cleaned.loc['(FORFEITED DEPOSITS)FEMALE']['ST']
            
       
        category = ["TOTAL","GEN", "SC", "ST"]
        

        value = [gen, sc, st_val]
        value.append(sum(value))

        total_female = pd.DataFrame({"caste Category": category, "Total FD": value})
            
        st.write(total_female)
            
        fig = px.pie(total_female, values='Total FD', names='caste Category', title='Deposit Distribution for Female',
                         hole=0.5)  # Set the hole parameter to 0.5 to create a donut chart
        st.plotly_chart(fig)
def third_gender():
        gen = dataset5_cleaned.loc['(FORFEITED DEPOSITS)THIRD GENDER']['GEN']
        sc = dataset5_cleaned.loc['(FORFEITED DEPOSITS)THIRD GENDER']['SC']
        st_val = dataset5_cleaned.loc['(FORFEITED DEPOSITS)THIRD GENDER']['ST']
        category = ["TOTAL","GEN", "SC", "ST"]
        value = [gen, sc, st_val]
        value.append(sum(value))

        total_third_gender = pd.DataFrame({"caste Category": category, "Total FD": value})
        st.write(total_third_gender)
        fig = px.pie(total_third_gender, values='Total FD', names='caste Category', title='Deposit Distribution for Third Gender',
                         hole=0.5)  # Set the hole parameter to 0.5 to create a donut chart
        st.plotly_chart(fig)

def fd_payed_categorywise():
    def categorywise(value):
        category_wise = dataset5_cleaned.loc['(FORFEITED DEPOSITS)MALE'][value] + dataset5_cleaned.loc['(FORFEITED DEPOSITS)FEMALE'][value] + dataset5_cleaned.loc['(FORFEITED DEPOSITS)THIRD GENDER'][value]
        return category_wise

    category = ["TOTAL", "GEN", "SC", "ST"]
    value = [categorywise('GEN'), categorywise('SC'), categorywise('ST')]
    total_value = sum(value)
    value.insert(0, total_value)
    total_fd_deposite = pd.DataFrame({"caste category": category, "Total_FD": value})
    trans = total_fd_deposite.transpose()
    st.dataframe(trans)
    fig = px.pie(total_fd_deposite, values='Total_FD', names='caste category')
    st.write(fig)
def nomination_fd_payed_by_each_category(caste):
    nomination_fd_payed_male = dataset5_cleaned.loc['(NOMINATIONS REJECTED)MALE'][caste]
    nomination_fd_payed_female= dataset5_cleaned.loc['(NOMINATIONS REJECTED)FEMALE'][caste]
    nomination_fd_payed_thirdgen = dataset5_cleaned.loc['(NOMINATIONS REJECTED)THIRD GENDER'][caste]
            
    category = ["TOTAL SUBMISSION", "MALE", "FEMALE", "THIRDGENDER"]
    value = [nomination_fd_payed_male, nomination_fd_payed_female, nomination_fd_payed_thirdgen]
    value.insert(0, sum(value))

    total_nomination_fd_payed= pd.DataFrame({"caste Category": category, "No_of_nomination": value})
    trans = total_nomination_fd_payed.transpose()
    st.dataframe(trans)
    fig = px.line(total_nomination_fd_payed, x='caste Category', y='No_of_nomination')
    st.write(fig)     

if button5:
    st.header("Analysis of Forfeited Deposits in Electoral Candidates")
    st.caption("""Our analysis delves into the forfeiture of deposits made by electoral candidates,
                        offering insights into financial penalties incurred during the nomination process.
                         Through meticulous examination, we explore forfeiture trends across different dimensions,
                        shedding light on gender-specific and category-specific patterns. Join us as we uncover the
                        implications of forfeited deposits on candidate participation and electoral dynamics.""")
    tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8=st.tabs(["TOTAL FORFEITED DEPOSITS  gender-wise",
         "TOTAL FORFEITED DEPOSITS OF MALE CANDIDATES ACROSS  CASTE CATEGORY",
         "TOTAL FORFEITED DEPOSITS OF FEMALE CANDIDATES ACROSS CASTECATEGORY",
         "TOTAL FORFEITED DEPOSITS OF THIRDGENDER CANDIDATES ACROSS CASTE CATEGORY",
         "TOTAL FORFEITED DEPOSITS  caste category-wise",
         "Total nomination FORFEITED DEPOSITS  in  GEN category across gender(2021)", 
         "Total nomination FORFEITED DEPOSITS  in  SC across gender(2021)", 
         "Total nomination FORFEITED DEPOSITS  in  ST cross gender(2021)"])
            
            
    with tab1:
        fd_payed_genderwise()
    with tab2:
        male()
    with tab3:
        female()
    with tab4:
        third_gender()
    with tab5:
        fd_payed_categorywise()
    with tab6:
        nomination_fd_payed_by_each_category('GEN')
    with tab7:
        nomination_fd_payed_by_each_category('SC')
    with tab8:
        nomination_fd_payed_by_each_category('ST')
        
