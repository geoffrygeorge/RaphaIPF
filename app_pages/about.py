import streamlit as st
import base64
from pathlib2 import Path

def about_page():

    ## ABOUT BACKGROUND
    ## SVG ENCODER FOR BACKGROUND
    def add_bg_from_local(SVG_FILE):  
        with open(SVG_FILE, "rb") as SVG_FILE:
            encoded_string = base64.b64encode(SVG_FILE.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"svg+xml"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )

    add_bg_from_local('images/SHINY.svg')
