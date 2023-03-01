"""
RAPHA INTERNATIONAL MINISTRIES Streamlit Web App
------------------------------------------------
Author & Maintainer: Geoffry
------------------------------------------------
Project Start Date: 20th February, 2023
"""

# ----- IMPORTING NECESSARY LIBRARIES -----
import streamlit as st
from streamlit_option_menu import option_menu
from app_pages import home, about


# ----- PAGE LAYOUT SETTINGS -----
# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "Rapha Int'l Ministries",
    page_icon = "Assets/images/RAPHA LOGO.png",
    initial_sidebar_state = "collapsed",
    layout = "wide"
)

def home_page_css(file_name):
    with open(file_name) as f:
        st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

home_page_css("assets/styles/home_page.css")


# ----- SIDEBAR -----
with st.sidebar:

    # custom sidebar option menu
    if False:
        MAIN_MENU = option_menu(
            "Main Menu", ["Home", "About Us"],
            icons = ["house", "info-circle"], 
            menu_icon = "menu-up", 
            default_index = 0, 
            orientation = "vertical")
    
    # default sidebar option menu
    MAIN_MENU = st.selectbox("MAIN MENU", ("Home", "About Us"))

# ----- HOME PAGE -----
if MAIN_MENU == "Home":

    home.home_page()

# ----- ABOUT US PAGE -----
if MAIN_MENU == "About Us":

    about.about_page()
