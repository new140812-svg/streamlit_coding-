import streamlit as st

# 페이지 설정 (브라우저 탭 이름과 아이콘)
st.set_page_config(page_title="김광희의 프로필", page_icon="👋")

# 헤더 부분
st.title("안녕하세요, 김광희입니다! 👋")
st.subheader("나를 소개하는 작은 공간")

# 레이아웃 나누기 (이미지나 강조하고 싶은 내용이 있을 때 유용)
col1, col2 = st.columns([1, 2])

with col1:
    # 프로필 이미지가 있다면 경로를 넣으세요. 없으면 이모지로 대체!
    st.title("👨‍💻") 

with col2:
    st.markdown("### **Who am I?**")
    st.write("- **정체성:** 사람임")
    st.write("- **이름:** 김광희")
    st.write("- **취미:** 놀기")

st.divider()

# 취미 섹션 상세화
st.header("🎮 My Hobby: Gaming")
st.info("저는 게임을 통해 전략을 짜고 새로운 세계를 탐험하는 것을 즐깁니다.")

# 인터랙티브 요소 추가 (선택 박스)
game_genre = st.selectbox(
    "광희님이 가장 좋아하는 게임 장르는?",
    ("RPG", "FPS", "시뮬레이션", "스포츠", "인디 게임")
)

st.write(f"아하! **{game_genre}** 장르를 좋아하시는군요! 저랑 취향이 비슷하신데요? 😉")
st.divider()
st.header("나의 코딩 실력")
st.markdown(
    """ 
        <a href="https://solved.ac/new140812/">
            <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=new140812" />
        </a>
    """,
    unsafe_allow_html=True
)




# 하단 푸터
st.caption("© 2026. 김광희 All rights reserved.")

