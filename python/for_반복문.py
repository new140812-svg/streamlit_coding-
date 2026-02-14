import streamlit as st
import time

st.set_page_config(page_title="for문 단계별 학습", layout="centered")

st.title("🏗️ for문: 아파트 층수 쌓기 학습기")
st.write("작성하신 필기 내용을 바탕으로 단계별 시뮬레이션을 구성했습니다.")

# 단계 구분을 위한 탭 생성
tabs = st.tabs(["1. 본질(꺼내기)", "2. 단순 반복", "3. 리스트 트릭", "4. 카운팅 변수", "5. range의 마법", "6. 최종 완성"])

# --- 1단계 ---
with tabs[0]:
    st.header("1. 바구니에서 하나씩 꺼내기")
    st.code("""
bag = ["컴퓨터", "신발", "책", "핸드크림"]
for i in bag:
    print(i)
    """)
    bag = ["컴퓨터", "신발", "책", "핸드크림"]
    if st.button("바구니 열어보기"):
        for item in bag:
            st.success(f"📦 {item}을(를) 꺼냈습니다.")
            time.sleep(0.5)

# --- 2단계 ---
with tabs[1]:
    st.header("2. 내용물 대신 다른 말 하기")
    st.code("""
for i in bag:
    print("감사합니다.")
    """)
    if st.button("인사하기"):
        for _ in bag:
            st.info("🙏 감사합니다.")

# --- 3단계 ---
with tabs[2]:
    st.header("3. 리스트 곱하기 트릭")
    st.code("""
for i in ["문자열"] * 10:
    print("아파트")
    """)
    if st.button("아파트 10번 출력"):
        for _ in ["문자열"] * 10:
            st.write("🏢 아파트")

# --- 4단계 ---
with tabs[3]:
    st.header("4. 층수 변수 직접 올리기")
    st.code("""
층수 = 1
for i in ["문자열"] * 10:
    print(f"아파트{층수}층")
    층수 = 층수 + 1
    """)
    if st.button("수동으로 층수 쌓기"):
        층수 = 1
        for _ in range(10):
            st.write(f"🏗️ 아파트 {층수}층")
            층수 += 1
            time.sleep(0.3)

# --- 5단계 ---
with tabs[4]:
    st.header("5. range와 * 의 차이")
    st.code("""
print(range(1, 11))
print(*range(1, 11))
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("그냥 range")
        st.warning(range(1, 11))
    with col2:
        st.subheader("풀어헤친(*range)")
        st.success(list(range(1, 11)))

# --- 6단계 ---
with tabs[5]:
    st.header("6. 가장 세련된 최종 완성")
    st.code("""
for i in range(1, 11):
    print(f"아파트{i}층")
    """)
    if st.button("최종 아파트 건설"):
        for i in range(1, 11):
            st.markdown(f"### 🏢 아파트 **{i}층** 완료")
            time.sleep(0.3)
        st.balloons()