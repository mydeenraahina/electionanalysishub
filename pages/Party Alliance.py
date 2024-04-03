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
url1 = "https://github.com/mydeenraahina/data_set/raw/main/Electors%20Data2.xlsx"
url2="
# Local file names to store the downloaded Excel files


file_1 = "Electors%20Data2.xlsx"
file_2="
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

dataset2 = pd.read_excel(url2,file_2)
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

# Cleaning dataset2 - PoliticalParties_ContestedSeats
class Clean_Dataset2:

    def droping_cols(self, dataset):
        # List of columns dropped from the DataFrame
        drop_columns = ["WON", "VOTES", "PERCENTAGE", "FD"]
        # Drop the specified columns
        dataset.drop(columns=drop_columns, inplace=True)

    def rename_cols(self, dataset):
        # Rename the column "ABBREVIATION" to "POLITICAL_PARTIES"
        dataset.rename(columns={"ABBREVIATION": "POLITICAL_PARTIES"}, inplace=True)

    def removing_empty_val(self, dataset):
        # Use the removing_empty_val method from Clean_Dataset1 to remove empty values
        cleaned_dataset1.removing_empty_val(dataset)

    def removing_duplicates(self, dataset):
        # Use the removing_duplicates method from Clean_Dataset1 to remove duplicate rows
        cleaned_dataset1.removing_duplicates(dataset)

    def setting_index(self, dataset):
        # Setting 'POLITICAL_PARTIES' as the index
        dataset.set_index('POLITICAL_PARTIES', inplace=True)

    def cleaned_data(self, dataset):
        # Apply cleaning steps
        self.droping_cols(dataset)
        self.rename_cols(dataset)
        self.removing_empty_val(dataset)
        self.removing_duplicates(dataset)
        self.setting_index(dataset)
        return dataset

# Create an instance of Clean_Dataset2
cleaned_dataset2 = Clean_Dataset2()
dataset2_cleaned = cleaned_dataset2.cleaned_data(dataset2)




def parties_cons(party,party_name):
            total_constituencies_data = dataset1_cleaned.loc['NO. OF CONSTITUENCIES']

            # Create a new DataFrame with the extracted data
            total_constituencies_table = pd.DataFrame({'Category': total_constituencies_data.index, 'Total_Constituencies': total_constituencies_data.values})
            total_constituencies_table_name = 'Total_Constituencies(2021)'
            total_constituencies_sum = total_constituencies_data.sum()
            party_constest = dataset2_cleaned.loc[party]['CONTESTED']
            df=pd.DataFrame({"Party":['Total Constituence TN Election 2021',party],"seats":[total_constituencies_sum,party_constest]})
            st.write(f"Seat Distribution of {party}")
            st.write(df)
            fig=px.bar(df,x="seats",y="Party",title=party_name)
            st.write(fig)

def Secular_Progressive_Alliance():
    
    def secularr_progressive_parties_contestment(party):
        parties_contest=dataset2_cleaned.loc[party]['CONTESTED']
        return parties_contest
    spa_parties=["DMK","INC","CPI","CPI(M)","VCK","MDMK","MMUK","IUML","KMDK","MMK","AIFB","TVK","MVK","ATP"]
    dmk=secularr_progressive_parties_contestment(spa_parties[0])
    inc=secularr_progressive_parties_contestment(spa_parties[1])
    cpi=secularr_progressive_parties_contestment(spa_parties[2])
    cpim=secularr_progressive_parties_contestment(spa_parties[3])
    vck=secularr_progressive_parties_contestment(spa_parties[4])
    mdmk=secularr_progressive_parties_contestment(spa_parties[5])
    mmuk=secularr_progressive_parties_contestment(spa_parties[6])
    iuml=secularr_progressive_parties_contestment(spa_parties[7])
    kmdk=secularr_progressive_parties_contestment(spa_parties[8])
    mmk=secularr_progressive_parties_contestment(spa_parties[9])
    aifb=secularr_progressive_parties_contestment(spa_parties[10])
    tvk=secularr_progressive_parties_contestment(spa_parties[11])
    mvk=secularr_progressive_parties_contestment(spa_parties[12])
    atp=secularr_progressive_parties_contestment(spa_parties[13])
    spa_seats_allince=[dmk,inc,cpi,cpim,vck,mdmk,mmuk,iuml,kmdk,mmk,aifb,tvk,mvk,atp]
    Total_spa_allince_parties = pd.DataFrame({"SPAparties": spa_parties, "Contested seats": spa_seats_allince})
    st.subheader(" Seat Distribution  Secular Progressive Alliance TN  (2021)")
    st.dataframe(Total_spa_allince_parties,width=1000)
    fig = px.pie(Total_spa_allince_parties ,values='Contested seats', names='SPAparties',title=' Secular Progressive Alliance TN 2021',width=800, height=600)
    st.write(fig)
    



st.markdown("<h1 style='color: #ff0066' ;> Party Alliance Taminadu Election 2021!</h1>", unsafe_allow_html=True)
st.write("Explore detailed insights in Party Alliance Taminadu Election 2021!")
st.write("""The Secular Progressive Alliance, led by the DMK, prioritized secularism and social justice, strategically distributing seats among its members for maximum impact. The National Democratic Alliance, spearheaded by the BJP, presented a conservative platform through parties like the ADMK, aiming to leverage seat allocation for electoral success. Independent parties pursued diverse agendas outside major alliances, reflecting regional interests and ideologies. The Peoples Front TN 2021, comprising various parties, strategically contested to address a wide range of electoral issues. Lastly, the People's First Alliance, uniting several parties, aimed to present a cohesive platform for addressing state concerns.""")
col1,col2=st.columns(2)
with col1:
    st.title(" Get Started!")
    st.write("🗳️ Explore insights into Party Alliance Click on the metric below to delve into the analysis!")

    
    



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
        st.markdown("🎯 SECULAR PROGRESSIVE ALLIANCE TAMILNADU ELECTION 2021", unsafe_allow_html=True)
        button1 = st.button("Click to View", key="button1", type="primary")
        st.markdown("🎯 NATIONAL DEMOCRATIC ALLIANCE TAMILNADU ELECTION 2021", unsafe_allow_html=True)
        button2 = st.button("Click to View", key="button2", type="primary")

        st.markdown("🎯 NON-ALIGNED PARTIES TAMILNADU ELECTION 2021", unsafe_allow_html=True)
        button3 = st.button("Click to View", key="button3", type="primary")
        

        

    with col2:
        st.markdown("🎯 PEOPLES FRONT TN 2021", unsafe_allow_html=True)
        button4 = st.button("Click to View", key="button4", type="primary")    
          

        st.markdown("🎯 TOP CONTESTED PARTIES TAMILNADU ELECTION 2021", unsafe_allow_html=True)
        button6 = st.button("Click to View", key="button6", type="primary")    

        st.markdown("🎯 MAXIMUM CONTESTED PARTIES TAMILNADU ELECTION 2021", unsafe_allow_html=True)
        button7 = st.button("Click to View", key="button7", type="primary")








   
    if button1:
    
        st.markdown("<h1 style='color: darkorange;'> Secular Progressive Alliance TN 2021</h1>", unsafe_allow_html=True)
        st.caption("""The Secular Progressive Alliance, led by the Dravida Munnetra Kazhagam (DMK),
                            emerged as a formidable force in the election. Comprising the DMK, Congress,
                            Communist Party of India (Marxist), Communist Party of India, Viduthalai Chiruthaigal Katchi,
                            and Indian Union Muslim League, this alliance focused on secularism, social justice,
                            and inclusive development as its core agenda.""")
        st.write("""To access detailed information about the Secular Progressive Alliance and its constituent parties,
                        kindly navigate to the respective tabs. The "Secular Progressive Alliance" tab will provide an overview
                        of the alliance's agenda and objectives, while individual tabs for each party within the alliance offer
                        insights into their contributions to the alliance's collective vision. Happy exploring!""")
        # Define tabs
        tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11,tab12,tab13,tab14,tab15= st.tabs(["Secular Progressive Alliance TN 2021","DMK contestment", "INC contestment", "CPI contestment","CPI(M) contestment","VCK contestment","MDMK contestment","MMUK contestment","IUML contestment","KMDK contestment","MMK contestment","AIFB contestment","TVK contestment","MVK contestment","ATP contestment"])
        
        with tab1:
            Secular_Progressive_Alliance()
        with tab2:
            parties_cons('DMK','DMK (Contestment TN 2021')

        with tab3:
            parties_cons('INC','INC Contestment TN 2021')
        with tab4:
            parties_cons('CPI','CPI  Contestment TN 2021')
        with tab5:
            parties_cons('CPI(M)','CPI(M) ( Contestment TN 2021')
        with tab6:
            parties_cons('VCK','VCK  Contestment TN 2021')
        with tab7:
            parties_cons('MDMK','MDMK  Contestment TN 2021')
        with tab8:
            parties_cons('MMUK','MMUK  Contestment TN 2021')
        with tab9:
            parties_cons('IUML','IUML  Contestment TN 2021')
        with tab10:
            parties_cons('KMDK','KMDK Contestment TN 2021')
        with tab11:
            parties_cons('MMK','MMK ( Contestment TN 2021')
        with tab12:
                parties_cons('AIFB','AIFB  Contestment TN 2021')
        with tab13:
                parties_cons('TVK','TVK Contestment TN 2021')
        with tab14:
                parties_cons('MVK','MVK  Contestment TN 2021')
        with tab15:
            parties_cons('ATP','ATP  Contestment TN 2021')

    def parties1_cons(party,party_name):
            total_constituencies_data = dataset1_cleaned.loc['NO. OF CONSTITUENCIES']

            # Create a new DataFrame with the extracted data
            total_constituencies_table = pd.DataFrame({'Category': total_constituencies_data.index, 'Total_Constituencies': total_constituencies_data.values})
            total_constituencies_table_name = 'Total_Constituencies(2021)'
            total_constituencies_sum = total_constituencies_data.sum()
            party_constest = dataset2_cleaned.loc[party]['CONTESTED']
            df=pd.DataFrame({"Party":['Total Constituence TN Election 2021',party],"seats":[total_constituencies_sum,party_constest]})
            st.write(f"Seat Distribution of {party}")
            st.write(df)
            fig=px.bar(df,x="seats",y="Party",title=party_name)
            st.write(fig)
    def National_Democratic_Alliance():
        
        
        
        def national_democratic_parties_contestment(party):
            parties_contest=dataset2_cleaned.loc[party]['CONTESTED']
            return parties_contest
        nda_parties=["ADMK","PMK","BJP","PTMK","TMMK","MMUK","AIMMK","PBK","PDK"]
            
        admk=national_democratic_parties_contestment(nda_parties[0])
        pmk=national_democratic_parties_contestment(nda_parties[1])
        bjp=national_democratic_parties_contestment(nda_parties[2])
        ptmk=national_democratic_parties_contestment(nda_parties[3])
        tmmk=national_democratic_parties_contestment(nda_parties[4])
        mmuk=national_democratic_parties_contestment(nda_parties[5])
        aimmk=national_democratic_parties_contestment(nda_parties[6])
        pbk=national_democratic_parties_contestment(nda_parties[7])
        pdk=national_democratic_parties_contestment(nda_parties[8])
        nda_seats_allince=[admk,pmk,bjp,ptmk,tmmk,mmuk,aimmk,pbk,pdk]
        
            
        Total_nda_allince_parties = pd.DataFrame({"NDAparties": nda_parties, "Contested seats": nda_seats_allince})
        trans= Total_nda_allince_parties.transpose()
        st.subheader(" Seat Distribution Among ADMK and its linked parties (2021)")
        st.dataframe(trans,width=1000)
        fig = px.pie(Total_nda_allince_parties ,values='Contested seats', names='NDAparties',title='National Democratic Alliance (2021)',width=800, height=600)
        st.write(fig)
    


    
        
    # Add button2 logic here
    if button2:
        st.markdown("<h1 style='color: teal;'>National Democratic Alliance</h1>", unsafe_allow_html=True)
        st.caption("""The National Democratic Alliance (NDA) is a centre-right to right-wing conservative
                                Indian political alliance led by the right-wing Bharatiya Janata Party (BJP).[2] It was
                                founded in 1998 and currently controls the government of India as well as the government
                                of 17 Indian states and one Union territory.""")
        st.caption("""The NDA was formed in May 1998 as a coalition to contest the general elections.
                                The main aim of the NDA was to form an anti-Indian National Congress coalition.
                                It was led by the BJP, and included several regional parties, including the Samata Party
                                and the AIADMK, as well as Shiv Sena, but Shiv Sena broke away from the alliance in
                                2019 to join the Maha Vikas Aghadi with Congress and the NCP. Samata Party is also broke
                                away from alliance in 2003 after formation of Janta Dal (United). The Shiv Sena was the only
                                member which shared the Hindutva ideology of the BJP.[5][6] After the election, it was able
                                to muster a slim majority with outside support from the Telugu Desam Party, allowing
                                Atal Bihari Vajpayee to return as prime minister.""")
        st.write("""To access detailed information about the National Democratic Alliance and its constituent parties,
                        kindly navigate to the respective tabs. The "National Democratic Alliance" tab will provide an overview
                        of the alliance's agenda and objectives, while individual tabs for each party within the alliance offer
                        insights into their contributions to the alliance's collective vision. Happy exploring!""")
        tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11=st.tabs(["National Democratic Alliance TN (2021)","ADMK contestment","PMK contestment","BJP contestment","TMC contestment",
            "PTMK contestment","TMMK contestment","MMUK contestment","AIMMK contestment","PBK contestment","PDK contestment"])
        with tab1:
            National_Democratic_Alliance()
        with tab2:
            parties1_cons('ADMK','ADMK (Contestment TN 2021')
        with tab3:
            parties1_cons('PMK','PMK (Contestment TN 2021')
        with tab4:
            parties1_cons('BJP','BJP (Barathiya Janatha party) Contestment TN 2021')
        with tab5:
            parties_cons('TMC','TMC  Contestment TN 2021')
        with tab6:
            parties_cons('PTMK','PTMK ( Contestment TN 2021')
        with tab7:
            parties_cons('TMMK','TMMK  Contestment TN 2021')
        with tab8:
            parties_cons('MMK','MMK Contestment TN 2021')
        with tab9:
            parties_cons('AIMMK','AIMMK Contestment TN 2021')
        with tab10:
            parties_cons('PBK','PBK  Contestment TN 2021')
        with tab11:
            parties_cons('PDK','PDK  Contestment TN 2021')




    def Non_aligned_parties():
        
                            
                                
        def Non_aligned_parties_contestment(party):
            parties_contest=dataset2_cleaned.loc[party]['CONTESTED']
            return parties_contest
        non_ap_parties=["NTK","BSP","PTK","CPI(ML)(L)","SAP"]
        ntk=Non_aligned_parties_contestment(non_ap_parties[0])
        bsp=Non_aligned_parties_contestment(non_ap_parties[1])
        ptk=Non_aligned_parties_contestment(non_ap_parties[2])
        cpimll=Non_aligned_parties_contestment(non_ap_parties[3])
        sap=Non_aligned_parties_contestment(non_ap_parties[4])
        non_ap_seats_allince=[ntk,bsp,ptk,cpimll,sap]
        
        Total_non_ap_allince_parties = pd.DataFrame({"NON_APparties":non_ap_parties, "Contested seats": non_ap_seats_allince})

        st.subheader(" Seat Contestment of   Non-aligned parties  TN  (2021)")
        st.dataframe(Total_non_ap_allince_parties ,width=1000)
        fig = px.bar(Total_non_ap_allince_parties ,x='Contested seats', y='NON_APparties',title='  Non-aligned parties TN 2021',width=800, height=600)
        st.write(fig)
    



    if button3:
        st.markdown("<h1 style='color: teal;'> Non-aligned parties TN 2021</h1>", unsafe_allow_html=True)
        st.caption("""Non-aligned parties in 2021 varied from region to region but typically included political
                            entities that were not affiliated with major political alliances or blocs. These parties often
                            pursued their own agendas, ideologies, or represented specific regional interests.""")
        st.write("""To access detailed information about the Non-Aligned Parties and their respective platforms,
                        kindly navigate to the respective tabs. The "Non-Aligned Parties" tab will provide an overview
                        of these parties' agendas and objectives. Individual tabs for each party within this category offer
                        insights into their history, ideology, and contributions to the political landscape. Happy exploring!""")
        tab1, tab2, tab3,tab4,tab5,tab6=st.tabs(["Non-aligned parties TN 2021","NTK contestment","BSP contestment","PTK contestment","CPI(ML)(L) contestment","SAP contestment"])
        with tab1:
            Non_aligned_parties()
        with tab2:
            parties_cons('NTK','NTK (Contestment TN 2021')
        with tab3:
            parties_cons('BSP','BSP Contestment TN 2021')
        with tab4:
            parties_cons('PTK','PTK  Contestment TN 2021')
        with tab5:
            parties_cons('CPI(ML)(L)','CPI(ML)(L) ( Contestment TN 2021')
        with tab6:
            parties_cons('SAP','SAP   Contestment TN 2021')
    def people_fronts():
        
                            
                                
        def people_fronts_parties(party):
            parties_contest=dataset2_cleaned.loc[party]['CONTESTED']
            return parties_contest
        non_ap_parties=["AMMKMNKZ","DMDK","SDPI","AIMIM"]
        ammkkmnkz=people_fronts_parties(non_ap_parties[0])
        dmdk=people_fronts_parties(non_ap_parties[1])
        psdpi=people_fronts_parties(non_ap_parties[2])
        aimim=people_fronts_parties(non_ap_parties[3])
        non_ap_seats_allince=[ammkkmnkz,dmdk,psdpi,aimim]
        
        Total_non_ap_allince_parties = pd.DataFrame({"party":non_ap_parties, "Contested seats": non_ap_seats_allince})

        st.subheader(" Seat Contestment of   Peoples Front  TN  (2021)")
        st.dataframe(Total_non_ap_allince_parties ,width=1000)
        fig = px.pie(Total_non_ap_allince_parties, values='Contested seats', names='party', title='Peoples Front TN (2021)', width=800, height=600)
        st.write(fig)
    
    if button4:
        st.markdown("<h1 style='color: teal;'> Peoples Front  TN  (2021)</h1>", unsafe_allow_html=True)
        st.write(""""Peoples Front TN (2021)" showcases the collaborative effort of various political parties in Tamil Nadu for the 2021 elections. This alliance represents a convergence of ideologies and agendas aimed at addressing the diverse needs and aspirations of the electorate. With parties like AMMK, MNK, and Z coming together under this front, it reflects a strategic coalition to consolidate support and amplify their impact on the electoral landscape. The inclusion of parties like DMDK, SDPI, and AIMIM further underscores the diversity and inclusivity of this coalition, catering to a wide spectrum of voters across the state. Together, these parties aim to offer a compelling vision and platform for governance, advocating for the welfare and progress of the people of Tamil Nadu.""")
        tab1, tab2, tab3,tab4,tab5=st.tabs(["People front parties TN 2021"," AMMKMNKZ contestment","DMDK contestment","SDPI contestment","AIMIM contestment"])
        with tab1:
            people_fronts()
        with tab2:
            parties_cons('AMMKMNKZ','AMMKMNKZ (Contestment TN 2021')
        with tab3:
            parties_cons('DMDK','DMDK Contestment TN 2021')
        with tab4:
            parties_cons('SDPI','SDPI  Contestment TN 2021')
        with tab5:
            parties_cons('AIMIM','AIMIM ( Contestment TN 2021')


    def people_alliance():
        
                            
                                
        def people_alliance_first(party):
            parties_contest=dataset2_cleaned.loc[party]['CONTESTED']
            return parties_contest
        non_ap_parties=["MNM","IJK","AISMK","TMJK","JDMK","JD(S)","KMI"]
        mnm=people_alliance_first(non_ap_parties[0])
        ijk=people_alliance_first(non_ap_parties[1])
        aismk=people_alliance_first(non_ap_parties[2])
        tmjk=people_alliance_first(non_ap_parties[3])
        jdmk=people_alliance_first(non_ap_parties[4])
        jds=people_alliance_first(non_ap_parties[5])
        kmi=people_alliance_first(non_ap_parties[6])
        non_ap_seats_allince=[(mnm,ijk,aismk,tmjk,jdmk,jds,kmi)]
        
        Total_non_ap_allince_parties = pd.DataFrame({"party": non_ap_parties, "Contested seats": [mnm, ijk, aismk, tmjk, jdmk, jds, kmi]})

        st.subheader(" Seat Contestment of   Peoples Front  TN  (2021)")
        st.dataframe(Total_non_ap_allince_parties ,width=1000)
        fig = px.pie(Total_non_ap_allince_parties, values='Contested seats', names='party', title='Peoples First Alliance TN (2021)', width=800, height=600)
        st.write(fig)
    
    
    def max_contested_parties_21():
            no_of_unique_parties=dataset2_cleaned.index.unique()
            max_seated_party=[]
            max_seated_parties_contested=[]
            for attemp in no_of_unique_parties:
                if dataset2_cleaned.loc[attemp]['CONTESTED'] >=25.0 and dataset2_cleaned.loc[attemp]['CONTESTED']<=234.0:
                    max_seated_party.append(attemp)
                    contested=dataset2_cleaned.loc[attemp]['CONTESTED']
                    max_seated_parties_contested.append(contested)
                
            maximum_no_of_seat_contested_parties=pd.DataFrame({"parties":max_seated_party,"no_of_seats_contested":max_seated_parties_contested})

            st.subheader(" Maximum no.of Seats Distribution Among Parties(2021)")
            st.dataframe(maximum_no_of_seat_contested_parties,width=1000)
            st.subheader("Exploring Maximum  Contested Parties in Tamil Nadu Election 2021")
            st.caption("""Our pie chart analysis of the Tamil Nadu Election 2021 reveals a diverse mix of contested parties,
                                    showcasing the state's vibrant political landscape. Traditional heavyweights like the DMK and
                                    AIADMK dominate the chart, alongside the growing influence of national parties like the BJP.
                                    Emerging regional players such as MNM also make a significant presence, reflecting the evolving
                                    preferences of Tamil Nadu's electorate. This diversity underscores the richness of democracy in the
                                    state, where multiple voices converge to shape the course of governance. As we delve into the data,
                                    we gain valuable insights into the complex socio-political fabric of Tamil Nadu.""")


            fig = px.pie(maximum_no_of_seat_contested_parties ,values='no_of_seats_contested', names='parties',title='MAXIMUM  NO . OF CONTESTED PARTIES  TAMILNADU ELECTION 2021',width=800, height=600)
            st.write(fig)
            
    if button7:
        st.markdown("<h1 style='color: teal;'>MAXIMUM CONTESTED PARTIES  TAMILNADU ELECTION 2021</h1>", unsafe_allow_html=True)
        st.caption("""The Tamil Nadu State Assembly elections of 2021 marked a significant chapter in the state's political history, characterized by
                                a plethora of contested parties vying for electoral success. With a diverse array of political ideologies and aspirations, the electoral
                                battleground witnessed the participation of major players like the DMK and AIADMK, alongside the burgeoning influence of parties such as the BJP and MNM.""")
        st.write("""To access detailed information about the Maximum Contested Parties in the 2021 election,
                        kindly navigate to the respective tabs. The "Maximum Contested Parties 2021" tab will provide an
                        overview of these parties' involvement and influence in the election. Individual tabs for each party
                        within this category offer insights into their campaign dynamics, electoral strategies, and impact on
                        the political landscape. Happy exploring!""")

        tab1, tab2, tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11,tab12,tab13,tab14,tab15,tab16=st.tabs(["MAXIMUM  NO . OF CONTESTED PARTIES  TAMILNADU ELECTION 2021","NTK contestment","ADMK contestment","DMK contestment","MNM contestment","AMMKMNKZ contestment","BSP contestment","DMDK contestment","MIDP contestment","IJK contestment","PT contestment","TNLK contestment","VTVTK contestment","AMPK contestment","INC contestment","APTADMK contestment"])
        with tab1:
            max_contested_parties_21()
        with tab2:
            parties_cons('NTK','NTK (Contestment TN 2021')
        with tab3:
            parties_cons('ADMK','ADMK  Contestment TN 2021')
        with tab4:
            parties_cons('DMK','DMK  Contestment TN 2021')
        with tab5:
            parties_cons('MNM','MNM  Contestment TN 2021')
        with tab6:
            parties_cons('AMMKMNKZ','AMMKMNKZ  Contestment TN 2021')
        with tab7:
            parties_cons('BSP','BSP  Contestment TN 2021')
        with tab8:
            parties_cons('DMDK','DMDK  Contestment TN 2021')
        with tab9:
            parties_cons('MIDP','MIDP  Contestment TN 2021')
        with tab10:
            parties_cons('IJK','IJK Contestment TN 2021')
        with tab11:
            parties_cons('PT','PT  Contestment TN 2021')
        with tab12:
            parties_cons('TNLK','TNLK  Contestment TN 2021')
        with tab13:
            parties_cons('VTVTK','VTVTK  Contestment TN 2021')
        with tab14:
            parties_cons('AMPK','AMPK  Contestment TN 2021')
        with tab15:
            parties_cons('INC','INC Contestment TN 2021')
        with tab16:
            parties_cons('APTADMK','APTADMK  Contestment TN 2021')


                
