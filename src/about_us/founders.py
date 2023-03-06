"""
OUR FOUNDERS SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
import base64

def founders_main():
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .founders {
                text-align: center;
                margin-bottom: 15px;
                font-size: calc(1.0em + 4vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'founders'>Our Founders</h2>", unsafe_allow_html = True)

    # FOUNDERS: IMAGE, NAME & DESC
    GEORGE_IMG_COL, GEORGE_DESC, MANOJ_IMG_COL, MANOJ_DESC = st.columns([1, 2, 1, 2])

    # GEORGE DETAILS
    with GEORGE_IMG_COL:
        def george_image(GEORGE_IMAGE):
            with open(GEORGE_IMAGE, "rb") as GEORGE_IMAGE:
                ENCODED_STRING = base64.b64encode(GEORGE_IMAGE.read())
            st.markdown(
                """
                <style>
                .george {
                    display: block;
                    max-width: 100%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .gzoom {
                    transition: transform .2s;
                }

                .gzoom:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="george gzoom">""", unsafe_allow_html = True)

        george_image("data/images/GEORGE.png")

    # GEORGE DESC
    with GEORGE_DESC:
        # NAME
        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .george_name {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("<h2 class = 'george_name'>Dr. George Mathew</h2>", unsafe_allow_html = True)

        # DESCRIPTION
        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .george_medium-font {
                    text-align: justify;
                    font-size: calc(1.0em + 0.5vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: medium;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("""<p class = "george_medium-font">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer venenatis vitae nulla a dictum.</p>""", unsafe_allow_html = True)

    # MANOJ DETAILS
    with MANOJ_IMG_COL:
        def manoj_image(MANOJ_IMAGE):
            with open(MANOJ_IMAGE, "rb") as MANOJ_IMAGE:
                ENCODED_STRING = base64.b64encode(MANOJ_IMAGE.read())
            st.markdown(
                """
                <style>
                .manoj {
                    display: block;
                    max-width: 100%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .mzoom {
                    transition: transform .2s;
                }

                .mzoom:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="manoj mzoom">""", unsafe_allow_html = True)

        manoj_image("data/images/MANOJ.png")

    # MANOJ DESC
    with MANOJ_DESC:
        # NAME
        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .manoj_name {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("<h2 class = 'manoj_name'>Br. Manoj Thomas</h2>", unsafe_allow_html = True)

        # DESCRIPTION
        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .manoj_medium-font {
                    text-align: justify;
                    font-size: calc(1.0em + 0.5vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: medium;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("""<p class = "manoj_medium-font">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer venenatis vitae nulla a dictum.</p>""", unsafe_allow_html = True)
