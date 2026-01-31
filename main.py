import streamlit as st

pages = {
    "streamlit": [
        st.Page("streamlit/S.py", title="STREAMLIT"),
    ],
    "AI": [
        st.Page("AI/A.py", title="AI"),  
    ],
}

pg = st.navigation(pages)
pg.run()