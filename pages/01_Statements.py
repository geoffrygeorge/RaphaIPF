"""
STATEMENTS PAGE
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
from streamlit_extras.app_logo import add_logo
import base64
from src.statements import faith, core_value, message, vision, mission
from src import processors


# ----- PAGE LAYOUT SETTINGS -----
# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "Mission Statements - Rapha Int'l Ministries",
    page_icon = "data/images/RAPHA LOGO.png",
    initial_sidebar_state = "collapsed",
    layout = "wide"
)

processors.app_style("styles/style.css")

# sidebar rapha logo
# add_logo("data/images/RAPHA_SIDEBAR.png")

# ----- STATEMENTS BACKGROUND -----
processors.svg_bg("data/images/SHINY.svg")


# ----- FAITH STATEMENT -----
with st.container():
    
    faith.faith_main()

# ----- CORE-VALUE STATEMENT -----
with st.container():

    core_value.core_value_main()

# ----- MESSAGE STATEMENT -----
with st.container():

    message.message_main()

# ----- VISION STATEMENT -----
with st.container():

    vision.vision_main()

# ----- MISSION STATEMENT -----
with st.container():

    mission.mission_main()
