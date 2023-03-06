"""
OUR MINISTRY SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st

def ministry_main():
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .ministry {
                text-align: center;
                margin-top:-50px;
                font-size: calc(1.0em + 4vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'ministry'>Our Ministry</h2>", unsafe_allow_html = True)

    # DESCRIPTION
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .ministry_medium-font {
                text-align: justify;
                font-size: calc(1.0em + 0.5vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: medium;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("""<p class = "ministry_medium-font">Our ministry is called <strong>'Rapha International Prayer Fellowship'</strong>. 'Rapha' means healer because our God is the healer. We praise our Lord God and His name is <strong>Jesus</strong>. He had no servants, yet they called Him <strong>Master</strong>. He had no worldly educational qualifications, yet they called Him <strong>Teacher</strong>. He had no medicines, yet they called Him <strong>Healer</strong>. He had no army, yet Kings feared Him. He won no military battles, yet He conquered the world through His Love. He committed no crime, yet they crucified Him. He was then buried in a tomb, and yet <strong>HE LIVES FOREVER AND EVER</strong>.</p>""", unsafe_allow_html = True)
