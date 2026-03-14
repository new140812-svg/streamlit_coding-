import streamlit as st

pages ={
    "about_me": [
        st.Page("about_me/자기소개.py", title="자기소개"),
    ],
    "python": [
        st.Page("python/for_반복문.py", title="for_반복문"),  
        st.Page("python/whlie_반복문.py", title="whlie_반복문"),
        st.Page("python/set_자료형.py", title="set_자료형"),  
        ],
    "streamlit": [
        st.Page("streamlit/text.py", title="text"),
        st.Page("streamlit/media.py", title="media"),

    ],
    "알고리즘": [
        st.Page("알고리즘/알고리즘이란.py", title="알고리즘이란"),
    ],
    "AI": [
        st.Page("AI/A.py", title="AI"),  
    ],
}

pg = st.navigation(pages)
pg.run()