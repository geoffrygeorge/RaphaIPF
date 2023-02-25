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
