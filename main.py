from dotenv import load_dotenv
import os
from DataDownload import datadownload
from Insights import insights
from charts import charts
from mysqlmigration import datamigration
from portfolio import portfolio
from preprocess import preprocessdata


import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(layout="wide")


def page_home():
    st.markdown(
        '''
        <div style="background: linear-gradient(to left, #800080, #FFD700); padding: 20px; border-radius: 5px;">
            <h1 style="color:#FFF; text-align: center;">Welcome to GitHub Data Dive</h1>
        </div><br>
        ''',
        unsafe_allow_html=True
    )
    intro_text = """
    In the dynamic world of open-source software, discovering valuable projects and understanding development trends is essential for developers, researchers, and organizations alike. 

    <span style='color:blue;'>GitHub Data Dive harnesses the power of the GitHub API to provide a comprehensive analysis of repositories across ten trending topics in the data landscape, including machine learning, data visualization, and natural language processing</span>.

    Explore repository characteristics such as stars, forks, programming languages, and more, all presented through an interactive and user-friendly Streamlit application. Whether you're looking for collaboration opportunities, analyzing technology trends, or sourcing educational materials, GitHub Data Dive equips you with the insights needed to navigate the open-source ecosystem effectively.

    Dive in and uncover the trends shaping the future of software development!
    """
    st.write(intro_text , unsafe_allow_html=True)
    st.markdown('<div style="color:blue; font-size: 24px;">'
                'Dive in and uncover the trends shaping the future of software development </div>'
                '<br><div style="color:green; font-size: 24px;">Enjoy exploring!</div>', unsafe_allow_html=True)

def  page_DataProcess():
    st.markdown(
        '''
        <div style="background: linear-gradient(to right, #32CD32, #FFD700); padding: 20px; border-radius: 5px;">
            <h1 style="color:#FFF; text-align: center;">Fetch Pre-Process and clean Data here  </h1>
        </div><br>
        ''',
        unsafe_allow_html=True
    )
    load_dotenv()
    api_key = os.getenv('API_KEY')

    topics = [
        "All",
        "Machine Learning",
        "Web Development",
        "Data Science",
        "Blockchain",
        "DevOps",
        "Game Development",
        "Cybersecurity",
        "Internet of Things (IoT)",
        "Mobile Development",
        "Open Source Tools"
    ]
    st.markdown('<span style="color: orange; font-size: 30px; font-weight: bold;">Choose a trending topic to process:</span>',
                unsafe_allow_html=True)
    selected_topic = st.selectbox("", topics)

    st.write("<span style=color:red;>You selected:</span>", unsafe_allow_html=True)
    st.write(f"<span style=color:blue;>{selected_topic}</span>", unsafe_allow_html=True)


    if selected_topic=='All':
        topics = topics
    else:
        topics = [selected_topic]
    btn=st.button("Fetch and preprocess data")
    if btn:

        df = preprocessdata(topics, api_key)

        st.write(df)
        df.to_csv(f'{topics[0]}.csv')

        datadownload(topics[0])

def page_datamigration():
    topics = [
        "All",
        "Machine Learning",
        "Web Development",
        "Data Science",
        "Blockchain",
        "DevOps",
        "Game Development",
        "Cybersecurity",
        "Internet of Things (IoT)",
        "Mobile Development",
        "Open Source Tools"
    ]
    st.markdown(
        '<span style="color: orange; font-size: 30px; font-weight: bold;">Choose a topic to migrate data to Mysql:</span>',
        unsafe_allow_html=True)
    selected_topic = st.selectbox("", topics)

    st.write("<span style=color:red;>You selected:</span>", unsafe_allow_html=True)
    st.write(f"<span style=color:blue;>{selected_topic} for MySQL Migration</span>", unsafe_allow_html=True)
    migrate=st.button("Migrate")
    if migrate:
        datamigration(selected_topic)

def page_Charts():
    charts()

def page_Insights():
    insights()

def page_Personal_Portfolio():
    portfolio()


selected_page = option_menu(
    menu_title=None,
    options=["Home", "Data Process", "MySQL Migration","Charts","Insights","Personal Portfolio"],
    icons=["house", "file-earmark-text", "database", "bar-chart", "check-circle", "file-earmark-pdf"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "10!important", "background-color": "purple"},
        "icon": {"font-size": "18px"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "text - align": "justify",
            "margin": "0px",
            "background-color": "purple",
            "color": "#FFC0CB",
            "border-radius": "5px",
            "padding": "5px",
        },
        "nav-link-selected": {"background-color": "#FFED20", "font-size": "16px","font-weight":"10px","text-align": "center",
                              "color":"#00008A"},
    }
)


if selected_page == "Home":
    page_home()
elif selected_page == "Data Process":
    page_DataProcess()
elif selected_page=="MySQL Migration":
    page_datamigration()
elif selected_page == "Charts":
    page_Charts()
elif selected_page == "Insights":
    page_Insights()
elif selected_page == "Personal Portfolio":
    page_Personal_Portfolio()
