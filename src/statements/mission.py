"""
MISSION STATEMENT SECTION
"""

# ----- IMPORTING NECESSARY LIBRARIES
import streamlit as st

def mission_main():
    # TITLE
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .mission {
                text-align: center;
                margin-top: 15px;
                font-size: calc(1.0em + 4vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: bold;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("<h2 class = 'mission'>MISSION STATEMENT</h2>", unsafe_allow_html = True)

    # DESCRIPTION
    st.markdown("""
        <style>
            @import url(https://fonts.googleapis.com/css?family=Montserrat);
            .mission_medium-font {
                text-align: justify;
                font-size: calc(1.0em + 0.5vmin);
                font-family: 'Montserrat', sans-serif;
                font-weight: medium;
                color: white;
            }
        </style>
    """, unsafe_allow_html = True)

    st.markdown("""<p class = "mission_medium-font">Rapha International Ministries(RIM) has a mission which is God's mission. God's mission is well-stated in the Bible that Sin separated man from God, therefore man is separated from man; its outcome is a fallen state-total depravity of human society. Jesus is God in the flesh, sacrificed Himself on the cross of Calvary to lift up the human beings from the depravity and hell punishment. RIM is on an urgent mission that has its basis in the Gospel of Christ serving God, the church, and the world. As part of it, RIM is engaged in educational, spiritual, humanitarian, and church-planting missions.</p>""", unsafe_allow_html = True)
