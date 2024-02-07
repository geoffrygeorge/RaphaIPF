"""
FAITH STATEMENT SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st

def faith_main():
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .faith {
                text-align: center;
                margin-top:-50px;
                font-size: calc(1.0em + 4vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'faith'>FAITHS STATEMENT</h2>", unsafe_allow_html = True)

    # DESCRIPTION
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .faith_medium-font {
                text-align: justify;
                font-size: calc(1.0em + 0.5vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: medium;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("""<p class = "faith_medium-font">Rapha International Ministries (RIM). We hold the Bible-based belief system. Triune God - the Father, the Son, and the Holy Spirit, is the Creator of everything, the father of all true believers, transcendent and immanent. He alone is worthy to be worshiped. The Bible which contains 66 books alone is the inspired word of God, unchangeable, everlasting, infallible, and the final court for every issue. It holds that Jesus is the revealed God in the flesh and accepts His redemptive work on thecross of Calvary for all the world, and the redeemed community of the Church. He is the final judge of the world. It also holds that God the Spirit is preparing the universal church of God at present and the belief in the everlasting destiny of man, heaven or hell.</p>""", unsafe_allow_html = True)
