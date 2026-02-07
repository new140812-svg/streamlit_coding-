import streamlit as st

pages ={
    "about_me": [
        st.Page("about_me/자기소개.py", title="자기소개"),
    ],
    
    "streamlit": [
        st.Page("streamlit/text.py", title="text"),
    ],
    "AI": [
        st.Page("AI/A.py", title="AI"),  
    ],
}

pg = st.navigation(pages)
pg.run()