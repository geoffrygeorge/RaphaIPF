"""
ABOUT US PAGE
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
import base64


# ----- PAGE LAYOUT SETTINGS -----
# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "About Us",
    page_icon = "Assets/images/RAPHA LOGO.png",
    initial_sidebar_state = "collapsed",
    layout = "wide"
)

def app_style(file_name):
    with open(file_name) as f:
        st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

app_style("Assets/styles/app_style.css")


# ----- ABOUT US BACKGROUND -----
def about_bg(SVG_IMAGE):
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

about_bg("Assets/images/SHINY.svg")

# ----- OUR MINISTRY -----
with st.container():
    
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

# ----- OUR FOUNDERS -----
with st.container():

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
                    max-width: 80%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .gzoom {
                    transition: transform .2s;
                }

                .gzoom:hover {
                    transform: scale(1.10);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="george gzoom">""", unsafe_allow_html = True)

        george_image("Assets/images/GEORGE.png")

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

        st.markdown("""<p class = "george_medium-font">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer venenatis vitae nulla a dictum. Suspendisse tempus convallis felis a dictum. Aliquam bibendum molestie orci maximus porta.</p>""", unsafe_allow_html = True)

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
                    max-width: 80%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                }

                .mzoom {
                    transition: transform .2s;
                }

                .mzoom:hover {
                    transform: scale(1.10);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="manoj mzoom">""", unsafe_allow_html = True)

        manoj_image("Assets/images/MANOJ.png")

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

        st.markdown("""<p class = "manoj_medium-font">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer venenatis vitae nulla a dictum. Suspendisse tempus convallis felis a dictum. Aliquam bibendum molestie orci maximus porta.</p>""", unsafe_allow_html = True)
