"""
CORE-VALUE STATEMENT SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st

def core_value_main():
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .corevalue {
                text-align: center;
                margin-top:-50px;
                font-size: calc(1.0em + 4vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'corevalue'>CORE-VALUE STATEMENT</h2>", unsafe_allow_html = True)

    # DESCRIPTION
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .corevalue_medium-font {
                text-align: justify;
                font-size: calc(1.0em + 0.5vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: medium;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("""<p class = "corevalue_medium-font">Since Christianity is anchored on core values that are considered fundamental to living a life dedicated to serving God and others Rapha International Ministries is committed to abide on these values. Such values provide a moral compass for all holistic mission activities of Rapha International Ministries worldwide. It follows the values such as:</p>""", unsafe_allow_html = True)
