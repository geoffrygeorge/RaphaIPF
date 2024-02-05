"""
MESSAGE STATEMENT SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st

def message_main():
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .message {
                text-align: center;
                margin-top: 15px;
                font-size: calc(1.0em + 4vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'message'>MESSAGE STATEMENT</h2>", unsafe_allow_html = True)

    # DESCRIPTION
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .message_medium-font {
                text-align: justify;
                font-size: calc(1.0em + 0.5vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: medium;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("""<p class = "message_medium-font">Rapha International Ministries (RIM) has an absolute message to the world that man is irrecoverably lost and any human attempt to overcome it will be an absolute failure. The Gospel of Christ is the philosophy of God as a perfect solution for human recovery from the lost state.</p>""", unsafe_allow_html = True)
