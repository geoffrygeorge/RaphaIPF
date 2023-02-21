##### RAPHA INTERNATIONAL MINISTRIES Streamlit Web App #####
##### Author & Maintainer: Geoffry #####
##### Date: 20th February, 2023 #####

"""importing libraries"""
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import base64
from pathlib import Path

# PAGE LAYOUT SETTINGS

# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "Rapha Int'l Ministries",
    page_icon = "Assets/images/RAPHA LOGO.png",
    initial_sidebar_state = "auto",
    layout = "wide",
)

# HIDE HEADER MENU & FOOTER

# class {background: rgba(0,0,0,0.5);}
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html = True)

# DEFINING SIDEBAR MENUS

with st.sidebar:
    MAIN_MENU = option_menu(
        "Main Menu", ["Home"],
        icons = ["house"], menu_icon = "cast", default_index = 0)

### HOME ###
if MAIN_MENU == "Home":

    ## HOME BACKGROUND
    # background resources: https://unsplash.com/s/photos/prayer
    # Photo by <a href="https://unsplash.com/@patrickian4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Patrick Fore</a> on <a href="https://unsplash.com/s/photos/prayer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
    def home_bg(HOME_BG_IMAGE):
        """function definition concerning HOME bg image"""
        with open(HOME_BG_IMAGE, "rb") as HOME_BG_IMAGE:
            ENCODED_STRING = base64.b64encode(HOME_BG_IMAGE.read())
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"jpg"};base64,{ENCODED_STRING.decode()});
                background-size: cover
            }}
            </style>
            """, unsafe_allow_html = True)

    home_bg("Assets/images/PRAY.jpg")

    ## RAPHA LOGO
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
            "<p style = 'text-align: center;'>"+img_to_html('Assets/images/RAPHA LOGO.png')+"</p>", unsafe_allow_html = True
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
                max-width: 100%;
                max-height: 100%;
                margin-left: auto;
                margin-right: auto;
                margin-top: -30px;
            }

            .zoom {
                transition: transform .2s;
            }

            .zoom:hover {
                transform: scale(1.05);
            }
            </style>
            """, unsafe_allow_html = True)
        
        st.markdown(
            f"""
            <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="zoom">""", unsafe_allow_html = True)

    home_logo("Assets/images/RAPHA LOGO.png")

    ## MAIN TITLE
    # <link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet'/>
    # https://www.justinmind.com/blog/best-google-web-fonts-website/
    st.markdown(
        """
        <style>
            @import url(https://fonts.googleapis.com/css?family=Roboto);
            .h1 {
                text-align: center;
                padding-top: 10px;
                font-size: calc(1.0em + 4.0vmin);
                font-family: 'Roboto', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
        """, unsafe_allow_html = True)

    st.markdown("<p class='h1'>RAPHA INTERNATIONAL MINISTRIES</p>", unsafe_allow_html = True)

    st.markdown("<h2 style='text-align: center; color: white;'>SINCE 2020</h2>", unsafe_allow_html = True)

    st.markdown(
        """
        <style>
        .css-eczf16 {display: none}
        </style>
        """, unsafe_allow_html = True)
