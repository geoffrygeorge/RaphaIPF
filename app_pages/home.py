# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st
import base64
from pathlib2 import Path


# ----- HOME FUNCTION DEFINITION -----
def home_page():
    """
    Function Definition consisting of various Home sections
    """

    # ----- HOME BACKGROUND -----
    # background resources: https://unsplash.com/s/photos/prayer
    # Photo by <a href="https://unsplash.com/@patrickian4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Patrick Fore</a> on <a href="https://unsplash.com/s/photos/prayer?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
    def home_bg(HOME_BG_IMAGE):
        """
        JPG Encoder for setting .jpg images as background(s)
        """
        with open(HOME_BG_IMAGE, "rb") as HOME_BG_IMAGE:
            ENCODED_STRING = base64.b64encode(HOME_BG_IMAGE.read())
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

    home_bg("Assets/images/PRAY.jpg")

    # ----- RAPHA LOGO AND MAIN TITLE(S) -----
    with st.container():

        # RAPHA LOGO
        # 1st method deprecated
        if False:
            def img_to_bytes(LOGO_PATH):
                IMG_BYTES = Path(LOGO_PATH).read_bytes()
                ENCODED = base64.b64encode(IMG_BYTES).decode()
                return ENCODED

            def img_to_html(LOGO_PATH):
                IMG_HTML = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(img_to_bytes(LOGO_PATH))
                return IMG_HTML

            st.markdown(
                "<p style = 'text-align: center;'>"+img_to_html('Assets/images/RAPHA LOGO.png')+"</p>", unsafe_allow_html = True
                )

        # 2nd updated method
        def home_logo(HOME_RAPHA_LOGO):
            with open(HOME_RAPHA_LOGO, "rb") as HOME_RAPHA_LOGO:
                ENCODED_STRING = base64.b64encode(HOME_RAPHA_LOGO.read())
            st.markdown(
                """
                <style>
                img {
                    display: block;
                    max-width: 50%;
                    max-height: auto;
                    margin-left: auto;
                    margin-right: auto;
                    margin-top: -30px;
                    padding-bottom: 30px;
                }

                .zoom {
                    transition: transform .2s;
                }

                .zoom:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html = True)
            
            st.markdown(
                f"""
                <img src = "data:image/{"png"};base64,{ENCODED_STRING.decode()}" class="zoom">""", unsafe_allow_html = True)

        home_logo("Assets/images/RAPHA LOGO.png")

        # MAIN TITLE
        # <link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet'/>
        # https://www.justinmind.com/blog/best-google-web-fonts-website/
        st.markdown(
            """
            <style>
                @import url(https://fonts.googleapis.com/css?family=Roboto);
                .h1 {
                    text-align: center;
                    font-size: calc(1.0em + 4.5vmin);
                    font-family: 'Roboto', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
            """, unsafe_allow_html = True)

        st.markdown("<p class = 'h1'>RAPHA INTERNATIONAL MINISTRIES</p>", unsafe_allow_html = True)
        
        # SECOND TITLE
        st.markdown(
            """
            <style>
                @import url(https://fonts.googleapis.com/css?family=Roboto);
                .h2 {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Roboto', sans-serif;
                    font-weight: bold;
                    color: white;
                }
            </style>
            """, unsafe_allow_html = True)

        st.markdown("<p class = 'h2'>Kingdom of Bahrain, since 2020</p>", unsafe_allow_html = True)

        if False:
            st.markdown("<h2 style = 'text-align: center; color: white;'>SINCE 2020</h2>", unsafe_allow_html = True)

            st.markdown(
                """
                <style>
                .css-eczf16 {display: none}
                </style>
                """, unsafe_allow_html = True)
            
        # BIBLE VERSE
        st.markdown("""
            <style>
                @import url(https://fonts.googleapis.com/css?family = Roboto);
                .medium-font {
                    text-align: center;
                    font-size: calc(1.0em + 1vmin);
                    font-family: 'Roboto', sans-serif;
                    font-weight: medium;
                    color: white;
                }
            </style>
        """, unsafe_allow_html = True)

        st.markdown("""<p class = "medium-font">"Philippians 4:13 - I can do all things through Christ Who strengthens me"</p>""", unsafe_allow_html = True)
