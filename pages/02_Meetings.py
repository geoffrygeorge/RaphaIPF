"""
MEETINGS PAGE
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
from streamlit_extras.app_logo import add_logo
import base64
from src import processors


# ----- PAGE LAYOUT SETTINGS -----
# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "Meetings - Rapha Int'l Ministries",
    page_icon = "data/images/RAPHA LOGO.png",
    initial_sidebar_state = "collapsed",
    layout = "wide"
)

processors.app_style("styles/meetings_style.css")

# sidebar rapha logo
add_logo("data/images/RAPHA_SIDEBAR.png")

# ----- MEETINGS BACKGROUND -----
processors.svg_bg("data/images/LUMINS.svg")


# ----- MEETINGS -----
with st.container():
    
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .meetings {
                text-align: center;
                margin-top:-50px;
                font-size: calc(1.0em + 4vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'meetings'>Meetings</h2>", unsafe_allow_html = True)
