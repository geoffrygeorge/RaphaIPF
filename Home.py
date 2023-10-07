"""
RAPHA INTERNATIONAL MINISTRIES Streamlit Web App
------------------------------------------------
Author & Maintainer: Geoffry
------------------------------------------------
Project Start Date: 20th February, 2023

Project Re-start Date: 07th October, 2023
------------------------------------------------
HOME PAGE
"""

# ----- IMPORTING NECESSARY LIBRARIES -----
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.app_logo import add_logo
import base64
from pathlib2 import Path
from src import processors


# ----- PAGE LAYOUT SETTINGS -----
# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "Home - Rapha Int'l Ministries",
    page_icon = "data/images/RAPHA LOGO.png",
    initial_sidebar_state = "collapsed",
    layout = "wide"
)

processors.app_style("styles/home_style.css")

# sidebar rapha logo
# add_logo("data/images/RAPHA_SIDEBAR.png")

# ----- HOME BACKGROUND -----
# background resources: https://unsplash.com/s/photos/prayer
# Photo by <a href="https://unsplash.com/@patrickian4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Patrick Fore</a> on <a href="https://unsplash.com/s/photos/prayer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
processors.jpg_bg("data/images/PRAY.jpg")


# ----- RAPHA LOGO AND MAIN TITLE(S) -----
with st.container():

    # RAPHA LOGO
    # 1st method deprecated
    if False:
        def img_to_bytes(LOGO_PATH):
            IMG_BYTES = Path(LOGO_PATH).read_bytes()
            ENCODED = base64.b64encode(IMG_BYTES).decode()
            return ENCODED

        def img_to_html(LOGO_PATH):
            IMG_HTML = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(img_to_bytes(LOGO_PATH))
            return IMG_HTML

        st.markdown(
            "<p style = 'text-align: center;'>"+img_to_html('data/images/RAPHA LOGO.png')+"</p>", unsafe_allow_html = True
            )

    # 2nd updated method
    def home_logo(HOME_RAPHA_LOGO):
        with open(HOME_RAPHA_LOGO, "rb") as HOME_RAPHA_LOGO:
            ENCODED_STRING = base64.b64encode(HOME_RAPHA_LOGO.read())
        st.markdown(
            """
            <style>
            img {
                display: block;
                max-width: 40%;
                max-height: auto; 
                margin-left: auto; /* or margin: 0 auto; */
                margin-right: auto;
                margin-top: -30px;
                padding-bottom: 30px;
            }

            .logo {
                transition: transform .2s;
            }

            .logo:hover {
                transform: scale(1.10);
            }
            </style>
            """, unsafe_allow_html = True)
        
        st.markdown(
            f"""
            <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="logo">""", unsafe_allow_html = True)

    home_logo("data/images/RAPHA LOGO.png")

    # MAIN TITLE
    # <link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet'/>
    # https://www.justinmind.com/blog/best-google-web-fonts-website/
    st.markdown(
        """
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .main_title {
                text-align: center;
                font-size: calc(1.0em + 4.5vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
        """, unsafe_allow_html = True)

    st.markdown("<h1 class = 'main_title'>RAPHA INTERNATIONAL MINISTRIES</h1>", unsafe_allow_html = True)
    
    # SECOND TITLE
    st.markdown(
        """
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .second_title {
                text-align: center;
                font-size: calc(1.0em + 1vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
        """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'second_title'>Kingdom of Bahrain, since 2020</h2>", unsafe_allow_html = True)
        
    # BIBLE VERSE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .verse_medium-font {
                text-align: center;
                font-size: calc(1.0em + 1vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: medium;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("""<p class = "verse_medium-font">"Philippians 4:13 - I can do all things through Christ Who strengthens me"</p>""", unsafe_allow_html = True)
