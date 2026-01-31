import streamlit as st
st.title("이건 AI")
st.header("김광희")
st.subheader("....")
st.write("Hi")
나이 = st.slider("너의 나이는?", 0, 100)
st.write(f"너의 아이는 {나이}살이구나")
눌렀다 = st.toggle("버튼")
if 눌렀다 == True:
    st.write("생일 축하해!")
    st.balloons()
else:
    st.write("생일 축하안함.")
