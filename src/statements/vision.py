"""
VISION STATEMENT SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st

def vision_main():
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .vision {
                text-align: center;
                margin-top: 15px;
                font-size: calc(1.0em + 4vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'vision'>VISION STATEMENT</h2>", unsafe_allow_html = True)

    # DESCRIPTION
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .vision_medium-font {
                text-align: justify;
                font-size: calc(1.0em + 0.5vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: medium;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("""<p class = "vision_medium-font">Rapha International Ministries(RIM) is a vision-oriented NGO; its vision is Christ-centered vision; Christ's vision is holistic to restore the human society from all bondages. RIM is committed to taking any risk to crystallize Christ's vision which is the nucleus of the great commission of Jesus Christ. Preaching and teaching are the parts of the great commission in order to produce the right disciples. The right disciples can only become right citizens of the world, therefore RIM is engaged to make the right disciples who are right citizens of the world, thus the world will become better.</p>""", unsafe_allow_html = True)
