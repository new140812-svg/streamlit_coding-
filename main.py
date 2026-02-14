import streamlit as st

pages ={
    "about_me": [
        st.Page("about_me/자기소개.py", title="자기소개"),
    ],
    "python": [
        st.Page("python/for_반복문.py", title="for_반복문"),  
    ],
    "streamlit": [
        st.Page("streamlit/text.py", title="text"),
        st.Page("streamlit/media.py", title="media"),

    ],
    "AI": [
        st.Page("AI/A.py", title="AI"),  
    ],
}

pg = st.navigation(pages)
pg.run()