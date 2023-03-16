import streamlit as st
import base64


# ----- JPG ENCODER -----
def jpg_bg(JPG_IMAGE):
    """
    JPG Encoder for setting .jpg images as background(s)
    """
    with open(JPG_IMAGE, "rb") as JPG_IMAGE:
        ENCODED_STRING = base64.b64encode(JPG_IMAGE.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpg"};base64,{ENCODED_STRING.decode()});
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-size: cover;
        }}
        </style>
        """, unsafe_allow_html = True)

# ----- SVG ENCODER -----
def svg_bg(SVG_IMAGE):
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
