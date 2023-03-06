"""
ABOUT US PAGE
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
import base64
from src.about_us import ministry, founders, ministers, techteam


# ----- PAGE LAYOUT SETTINGS -----
# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "About Us - Rapha Int'l Ministries",
    page_icon = "data/images/RAPHA LOGO.png",
    initial_sidebar_state = "collapsed",
    layout = "wide"
)

def app_style(file_name):
    with open(file_name) as f:
        st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

app_style("styles/about_style.css")


# ----- ABOUT US BACKGROUND -----
def about_bg(SVG_IMAGE):
    """
    SVG Encoder for setting .svg images as background(s)
    """
    with open(SVG_IMAGE, "rb") as SVG_IMAGE:
        ENCODED_STRING = base64.b64encode(SVG_IMAGE.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"svg+xml"};base64,{ENCODED_STRING.decode()});
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-size: cover;
        }}
        </style>
        """, unsafe_allow_html = True)

about_bg("data/images/SHINY.svg")

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
