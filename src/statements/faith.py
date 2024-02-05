"""
OUR MINISTRY SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st

def faith_main():
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

    st.markdown("<h2 class = 'ministry'>FAITH STATEMENT</h2>", unsafe_allow_html = True)

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

    st.markdown("""<p class = "ministry_medium-font">Rapha International Ministries (RIM)We holds the Bible-based believe system. Triune God-theFather,the Son and the Holy Spirit, is the Creator of everything, the father of all true believers,transcendent and immanent. He alone, is worthy to be worshiped. The Bible that contains 66 booksalone is the inspired word of God, unchangeable, everlasting, infallible and the final court for everyissue. It holds that Jesus is the revealed God in the flesh and accepts His redemptive work on thecross of Calvary for all world, and the redeemed community the Church. He is the final judge of theworld. It also holds that God the Spirit is preparing the universal church of God at present and thebelief on the everlasting destiny of man, heaven or hell.</p>""", unsafe_allow_html = True)
