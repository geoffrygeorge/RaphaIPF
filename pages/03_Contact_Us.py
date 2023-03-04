"""
CONTACT US PAGE
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
import base64


# ----- PAGE LAYOUT SETTINGS -----
# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "Contact Us - Rapha Int'l Ministries",
    page_icon = "Assets/images/RAPHA LOGO.png",
    initial_sidebar_state = "collapsed",
    layout = "wide"
)

def app_style(file_name):
    with open(file_name) as f:
        st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

app_style("Assets/styles/about_style.css")


# ----- CONTACT US BACKGROUND -----
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

about_bg("Assets/images/LUMINS.svg")