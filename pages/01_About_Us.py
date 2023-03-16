"""
ABOUT US PAGE
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
from streamlit_extras.app_logo import add_logo
import base64
from src.about_us import ministry, founders, ministers, techteam
from src import processors


# ----- PAGE LAYOUT SETTINGS -----
# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "About Us - Rapha Int'l Ministries",
    page_icon = "data/images/RAPHA LOGO.png",
    initial_sidebar_state = "collapsed",
    layout = "wide"
)

processors.app_style("styles/about_style.css")

# sidebar rapha logo
add_logo("data/images/RAPHA_SIDEBAR.png")

# ----- ABOUT US BACKGROUND -----
processors.svg_bg("data/images/SHINY.svg")


# ----- OUR MINISTRY -----
with st.container():
    
    ministry.ministry_main()

# ----- OUR FOUNDERS -----
with st.container():

    founders.founders_main()

# ----- OUR MINISTERS -----
with st.container():

    ministers.ministers_main()

# ----- TECHNICAL TEAM -----
with st.container():

    techteam.techteam_main()
