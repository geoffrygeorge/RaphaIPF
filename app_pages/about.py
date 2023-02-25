import streamlit as st
import base64
from pathlib2 import Path

def about_page():

    ## ABOUT BACKGROUND
    ## SVG ENCODER FOR BACKGROUND
    def about_bg(SVG_IMAGE):  
        with open(SVG_IMAGE, "rb") as SVG_IMAGE:
            encoded_string = base64.b64encode(SVG_IMAGE.read())
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"svg+xml"};base64,{encoded_string.decode()});
                background-position: center;
                background-attachment: fixed;
                background-repeat: no-repeat;
                background-size: cover;
            }}
            </style>
            """, unsafe_allow_html = True)

    about_bg('Assets/images/SHINY.svg')

    with st.container():

        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Roboto);
                .h2 {
                    text-align: center;
                    margin-top:-50px;
                    font-size: calc(1.0em + 4vmin);
                    font-family: 'Roboto', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<p class="h2">Our Ministry</p>', unsafe_allow_html = True)

        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Roboto);
                .medium-font {
                    text-align: justify;
                    margin-bottom:70px;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Roboto', sans-serif;
                    font-weight: medium;
                    color: white;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("""<p class="medium-font">Our ministry is called <strong>'Rapha International Prayer Fellowship'</strong>. 'Rapha' means healer because our God is the healer. We praise our Lord God and His name is <strong>Jesus</strong>. He had no servants, yet they called Him <strong>Master</strong>. He had no worldly educational qualifications, yet they called <strong>Teacher</strong>. He had no medicines, yet they called him <strong>Healer</strong>. He had no army, yet Kings feared Him. He won no military battles, yet He conquered the world through His Love. He committed no crime, yet they crucified Him. He was then buried in a tomb, and yet <strong>HE LIVES FOREVER AND EVER</strong>.</p>""", unsafe_allow_html = True)
