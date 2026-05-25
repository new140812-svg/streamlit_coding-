import streamlit as st
import random

# 페이지 레이아웃 및 제목 설정
st.title("✊✌️🖐️ 게임 실습 1: 가위 바위 보")
st.write("구글 코랩에서 직접 작성하고 공부했던 가위바위보 알고리즘입니다.")

# 1단계(조건문)와 2단계(인덱스 연산)를 탭으로 분할하여 학습 내용 비교
tab1, tab2 = st.tabs(["💡 1단계: 기본 조건문 방식", "🧠 2단계: 똑똑한 인덱스 수학 방식"])

# --- 1단계: 기본 조건문 방식 ---
with tab1:
    st.subheader("1단계: 조건문(if-elif)으로 판정하기")
    st.info("컴퓨터의 선택과 나의 선택을 조건문으로 일일이 비교하는 직관적인 알고리즘입니다.")

    선택지 = ["가위", "바위", "보"]
    
    # 결과 유지를 위한 세션 상태 세팅
    if "stage1_computer" not in st.session_state:
        st.session_state.stage1_computer = None
    if "stage1_user" not in st.session_state:
        st.session_state.stage1_user = None

    나 = st.selectbox("나의 선택을 고르세요:", 선택지, key="user_select_1")

    if st.button("가위바위보 내기!", key="btn_1"):
        컴퓨터 = random.choice(선택지)
        st.session_state.stage1_computer = 컴퓨터
        st.session_state.stage1_user = 나

    # 게임 판정 논리 작동
    if st.session_state.stage1_computer is not None:
        u_val = st.session_state.stage1_user
        c_val = st.session_state.stage1_computer

        st.markdown(f"### 🧑 나: **{u_val}** vs  💻 컴퓨터: **{c_val}**")

        if c_val == "가위" and u_val == "바위":
            st.success("🎉 결과: 내가 이겼다! (나 Win)")
            st.balloons()
        elif c_val == "바위" and u_val == "보":
            st.success("🎉 결과: 내가 이겼다! (나 Win)")
            st.balloons()
        elif c_val == "보" and u_val == "가위":
            st.success("🎉 결과: 내가 이겼다! (나 Win)")
            st.balloons()
        elif c_val == u_val:
            st.warning("🤝 결과: 비겼습니다! (비김)")
        else:
            st.error("💀 결과: 컴퓨터가 이겼습니다! (컴퓨터 win)")


# --- 2단계: 똑똑한 인덱스 수학 방식 ---
with tab2:
    st.subheader("2단계: 리스트 인덱스 연산으로 판정하기")
    st.info("리스트의 인덱스 관계를 수학적으로 계산(컴퓨터선택 - 1, - 2)하여 코드를 획기적으로 축소한 방식입니다.")

    # 코랩에서 작성한 리스트 구조 반영
    선택지1 = ["가위", "바위", "보"]
    선택지2 = [0, 1, 2] # 가위(0), 바위(1), 보(2)

    if "stage2_computer_num" not in st.session_state:
        st.session_state.stage2_computer_num = None
    if "stage2_user" not in st.session_state:
        st.session_state.stage2_user = None

    나2 = st.selectbox("나의 선택을 고르세요:", 선택지1, key="user_select_2")

    if st.button("가위바위보 내기!", key="btn_2"):
        컴퓨터숫자 = random.choice(선택지2)
        st.session_state.stage2_computer_num = 컴퓨터숫자
        st.session_state.stage2_user = 나2

    # 수학적 인덱스 관계 분석을 통한 게임 판정 (컴퓨터숫자 - 1, 컴퓨터숫자 - 2 법칙 적용)
    if st.session_state.stage2_computer_num is not None:
        c_num = st.session_state.stage2_computer_num
        c_val2 = 선택지1[c_num]
        u_val2 = st.session_state.stage2_user

        st.markdown(f"### 🧑 나: **{u_val2}** vs  💻 컴퓨터: **{c_val2}** (컴퓨터 숫자 인덱스: {c_num})")

        # 1. 컴퓨터가 고른 인덱스에서 1을 뺀 자리에 내가 낸 것이 있다면 -> 컴퓨터가 이김 (내가 짐)
        if u_val2 == 선택지1[c_num - 1]:
            st.error("💀 결과: 내가 졌습니다... (내가짐)")
            
        # 2. 컴퓨터가 고른 인덱스에서 2를 뺀 자리에 내가 낸 것이 있다면 -> 내가 이김
        elif u_val2 == 선택지1[c_num - 2]:
            st.success("🎉 결과: 내가 이겼습니다! (내가이김)")
            st.balloons()
            
        # 3. 인덱스 위치가 어긋나지 않고 서로 같다면 -> 비김
        else:
            st.warning("🤝 결과: 서로 비겼습니다! (비김)")