"""
TECHNICAL TEAM SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
import base64

def techteam_main():
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .tech_team {
                text-align: center;
                margin-top: 15px;
                margin-bottom: 15px;
                font-size: calc(1.0em + 4vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'tech_team'>TECHNICAL TEAM</h2>", unsafe_allow_html = True)

    # TECHNICAL TEAM: IMAGE & NAME
    JEFF_IMG_COL, JOBIT_IMG_COL, DANNY_IMG_COL = st.columns(3)

    # JEFF DETAILS
    with JEFF_IMG_COL:
        def jeff_image(JEFF_IMAGE):
            with open(JEFF_IMAGE, "rb") as JEFF_IMAGE:
                ENCODED_STRING = base64.b64encode(JEFF_IMAGE.read())
            st.markdown(
                """
                <style>
                .jeff {
                    display: block;
                    max-width: 60%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .jzoom {
                    transition: transform .2s;
                }

                .jzoom:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="jeff pzoom">""", unsafe_allow_html = True)

        jeff_image("data/images/JEFF.png")

        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .jeff_name {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("<h2 class = 'jeff_name'>Br. Geoffry</h2>", unsafe_allow_html = True)
        st.markdown("<h2 class = 'jeff_name'>(Data Analyst & IT Head)</h2>", unsafe_allow_html = True)

    # JOBIT DETAILS
    with JOBIT_IMG_COL:
        def jobit_image(JOBIT_IMAGE):
            with open(JOBIT_IMAGE, "rb") as JOBIT_IMAGE:
                ENCODED_STRING = base64.b64encode(JOBIT_IMAGE.read())
            st.markdown(
                """
                <style>
                .jobit {
                    display: block;
                    max-width: 60%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .jozoom {
                    transition: transform .2s;
                }

                .jozoom:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="jobit jozoom">""", unsafe_allow_html = True)

        jobit_image("data/images/JOBIT.png")

        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .jobit_name {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("<h2 class = 'jobit_name'>Br. Jobit</h2>", unsafe_allow_html = True)
        st.markdown("<h2 class = 'jobit_name'>(Content Management Specialist)</h2>", unsafe_allow_html = True)

    # DANNY DETAILS
    with DANNY_IMG_COL:
        def danny_image(DANNY_IMAGE):
            with open(DANNY_IMAGE, "rb") as DANNY_IMAGE:
                ENCODED_STRING = base64.b64encode(DANNY_IMAGE.read())
            st.markdown(
                """
                <style>
                .danny {
                    display: block;
                    max-width: 60%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .dazoom {
                    transition: transform .2s;
                }

                .dazoom:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="danny dazoom">""", unsafe_allow_html = True)

        danny_image("data/images/DANNY.png")

        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .danny_name {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("<h2 class = 'danny_name'>Br. Danny</h2>", unsafe_allow_html = True)
        st.markdown("<h2 class = 'danny_name'>(Online Media Specialist)</h2>", unsafe_allow_html = True)
