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

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: rgba(52,152,219,0.5); backdrop-filter: blur(5px);">
  <a class="navbar-brand" href="#" target="_blank">Rapha Int'l Ministries</a>
</nav>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .css-jlsh98 {background: rgba(214,234,248,0.5); backdrop-filter: blur(5px);}
    footer {visibility: hidden;}
    /*footer:after {visibility: visible; 
                  content: "Copyright @ 2023: Rapha International Ministries";
                  display: block;
                  color: white;
                  }
    */
    .css-1nkmln7 {display: none} /*anchor link hidden*/
    .css-fblp2m {color: aqua; animation: zoom-in-zoom-out 1s ease infinite;} /*sidebar arrow animation*/

    @keyframes zoom-in-zoom-out {
    0% {
        transform: scale(1, 1);
    }

    50% {
        transform: scale(2, 2);
    }

    100% {
        transform: scale(1, 1);
    }
    }
    </style>
    """, unsafe_allow_html = True)

st.markdown("""
    <style>
    /*sidebar collapsed state*/
    .css-3m5iqg.e1fqkh3o1 {
        margin-top: 4rem;
    }

    /*sidebar expanded state*/
    .css-6qob1r.e1fqkh3o3 {
        margin-top: 4rem;
    }
    </style>
    """, unsafe_allow_html = True)

# ----- SIDEBAR MENUS -----
with st.sidebar:
    MAIN_MENU = st.selectbox("Main Menu", ("Home", "About Us"))

# ----- HOME PAGE -----
if MAIN_MENU == "Home":

    home.home_page()

# ----- ABOUT US PAGE -----
if MAIN_MENU == "About Us":

    about.about_page()
