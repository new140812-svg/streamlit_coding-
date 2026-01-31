import streamlit as st
st.title("This is a title")
st.header("This is a header")
st.subheader("This is subheader")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")
st.divider()
code = '''#include <stdio.h>

int main() {
    // 화면에 문장을 출력합니다.
    printf("Hello world\\n");
    
    return 0;
}'''
st.code(code, language="c")
if st.button("PLS Say hello"):
    st.write("Hello bro")
else:
    st.write("I not here")

st.divider()

st.write("당신은 일하고 싶습니까?")
agree = st.checkbox("나는 동의한다.")

if agree:
    st.write("아오지 탄광으로 보낼게.")