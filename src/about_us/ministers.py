"""
OUR MINISTERS SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
import base64

def ministers_main():
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .ministers {
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

    st.markdown("<h2 class = 'ministers'>Our Ministers</h2>", unsafe_allow_html = True)

    # MINISTERS: IMAGE & NAME
    PONN_IMG_COL, BIJU_IMG_COL, DHANISH_IMG_COL = st.columns(3)

    # PONNACHEN DETAILS
    with PONN_IMG_COL:
        def ponn_image(PONN_IMAGE):
            with open(PONN_IMAGE, "rb") as PONN_IMAGE:
                ENCODED_STRING = base64.b64encode(PONN_IMAGE.read())
            st.markdown(
                """
                <style>
                .ponn {
                    display: block;
                    max-width: 60%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .pzoom {
                    transition: transform .2s;
                }

                .pzoom:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="ponn pzoom">""", unsafe_allow_html = True)

        ponn_image("data/images/PONN.png")

        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .ponn_name {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("<h2 class = 'ponn_name'>Br. Ponnachen</h2>", unsafe_allow_html = True)

    # BIJU DETAILS
    with BIJU_IMG_COL:
        def biju_image(BIJU_IMAGE):
            with open(BIJU_IMAGE, "rb") as BIJU_IMAGE:
                ENCODED_STRING = base64.b64encode(BIJU_IMAGE.read())
            st.markdown(
                """
                <style>
                .biju {
                    display: block;
                    max-width: 60%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .bzoom {
                    transition: transform .2s;
                }

                .bzoom:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="biju bzoom">""", unsafe_allow_html = True)

        biju_image("data/images/BIJU.png")

        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .biju_name {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("<h2 class = 'biju_name'>Br. Biju</h2>", unsafe_allow_html = True)

    # DHANISH DETAILS
    with DHANISH_IMG_COL:
        def dhanish_image(DHANISH_IMAGE):
            with open(DHANISH_IMAGE, "rb") as DHANISH_IMAGE:
                ENCODED_STRING = base64.b64encode(DHANISH_IMAGE.read())
            st.markdown(
                """
                <style>
                .dhanish {
                    display: block;
                    max-width: 60%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .dzoom {
                    transition: transform .2s;
                }

                .dzoom:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="dhanish dzoom">""", unsafe_allow_html = True)

        dhanish_image("data/images/DHANISH.png")

        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family=Montserrat);
                .dhanish_name {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Montserrat', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("<h2 class = 'dhanish_name'>Br. Dhanish</h2>", unsafe_allow_html = True)
