"""
RAPHA INTERNATIONAL MINISTRIES Streamlit Web App
------------------------------------------------
Author & Maintainer: Geoffry
------------------------------------------------
Project Start Date: 20th February, 2023
"""

# ----- IMPORTING NECESSARY LIBRARIES
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

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    .css-jlsh98 {background: rgba(214,234,248,0.5); backdrop-filter: blur(30px);}
    footer {visibility: hidden;}
    /*footer:after {visibility: visible; 
                  content: "Copyright @ 2023: Rapha International Ministries";
                  display: block;
                  color: white;
                  }
    */
    </style>
    """, unsafe_allow_html = True)


# ----- SIDEBAR MENUS -----
with st.sidebar:
    MAIN_MENU = option_menu(
        "Main Menu", ["Home", "About Us"],
        icons = ["house", "info-circle"], 
        menu_icon = "menu-up", 
        default_index = 0, 
        orientation = "vertical")

# ----- HOME PAGE -----
if MAIN_MENU == "Home":

    home.home_page()

# ----- ABOUT US PAGE -----
if MAIN_MENU == "About Us":

    about.about_page()
