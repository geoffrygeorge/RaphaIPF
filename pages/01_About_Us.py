"""
ABOUT US PAGE
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
import base64


# ----- PAGE LAYOUT SETTINGS -----
# favicon_img = Image.open("images/Rapha-Logo.ico") ## this method is deprecated
st.set_page_config(
    page_title = "About Us - Rapha Int'l Ministries",
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

        st.markdown("""<p class = "manoj_medium-font">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer venenatis vitae nulla a dictum.</p>""", unsafe_allow_html = True)

# ----- OUR MINISTERS -----
with st.container():

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

        ponn_image("Assets/images/PONN.png")

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

        biju_image("Assets/images/BIJU.png")

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

        dhanish_image("Assets/images/DHANISH.png")

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

# ----- TECHNICAL TEAM -----
with st.container():

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

        jeff_image("Assets/images/JEFF.png")

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

        jobit_image("Assets/images/JOBIT.png")

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

        danny_image("Assets/images/DANNY.png")

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
