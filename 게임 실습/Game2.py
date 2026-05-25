import streamlit as st
import random
import time

st.set_page_config(page_title="게임실습 2: 메모리 게임", page_icon="🧠", layout="centered")

st.title("🧠 게임 실습 2: 순간 기억력 메모리 게임")
st.write("화면에 잠깐 나타났다 사라지는 숫자의 순서를 기억하고 똑같이 입력해 보세요!")

# 공부한 3가지 방식을 탭으로 선택할 수 있게 분할
tab1, tab2, tab3 = st.tabs(["🌱 1단계: 단판 승부", "🔄 2단계: 무한 누적", "❤️ 3단계: 라이프 시스템"])

# ==========================================================
# 💡 1단계: 단판 승부 방식
# ==========================================================
with tab1:
    st.subheader("1단계: 기초 단판 대결")
    st.info("컴퓨터가 생각한 1~3 사이의 숫자 1개를 아주 잠깐 보여줍니다. 기억했다가 맞춰보세요!")

    # 1단계 상태 관리 초기화
    if "stage1_step" not in st.session_state:
        st.session_state.stage1_step = "ready" # ready -> show -> input -> result
    if "stage1_number" not in st.session_state:
        st.session_state.stage1_number = None

    if st.session_state.stage1_step == "ready":
        if st.button("게임 시작! 🎮", key="s1_start"):
            st.session_state.stage1_number = random.randint(1, 3)
            st.session_state.stage1_step = "show"
            st.rerun()

    elif st.session_state.stage1_step == "show":
        # 숫자를 잠깐 노출하는 플레이스홀더 구성
        number_placeholder = st.empty()
        number_placeholder.markdown(f"<h1 style='text-align: center; color: #ff4b4b; font-size: 80px;'>{st.session_state.stage1_number}</h1>", unsafe_allow_html=True)
        time.sleep(0.7) # 코랩의 time.sleep(0.5)과 동일한 원리
        number_placeholder.empty() # 화면 지우기 (output.clear 역할)
        
        st.session_state.stage1_step = "input"
        st.rerun()

    elif st.session_state.stage1_step == "input":
        st.warning("⏱️ 화면에서 사라진 숫자는 무엇이었을까요?")
        user_input = st.number_input("기억한 숫자를 입력하세요 (1~3):", min_value=1, max_value=3, step=1, key="s1_input")
        
        if st.button("정답 확인 🔍", key="s1_submit"):
            if user_input == st.session_state.stage1_number:
                st.success("🎉 맞았다!")
                st.balloons()
            else:
                st.error(f"💀 틀렸다! 정답은 {st.session_state.stage1_number}였습니다.")
            
            # 다시하기를 위한 상태 초기화
            st.session_state.stage1_step = "ready"
            if st.button("다시 도전하기 🔁", key="s1_retry"):
                st.rerun()


# ==========================================================
# 🔄 2단계: 무한 누적 방식
# ==========================================================
with tab2:
    st.subheader("2단계: 무한 누적 도전")
    st.info("매 라운드마다 숫자가 하나씩 무작위로 계속 추가됩니다. 순서대로 정확하게 기억해서 입력해 보세요!")

    # 2단계 전용 세션 상태 관리 초기화
    if "s2_step" not in st.session_state:
        st.session_state.s2_step = "ready" # ready -> show -> input
    if "s2_list" not in st.session_state:
        st.session_state.s2_list = [] # 보여줄 숫자 리스트 L

    if st.session_state.s2_step == "ready":
        if st.button("도전 시작! 🚀", key="s2_start"):
            st.session_state.s2_list = [random.randint(1, 100)]
            st.session_state.s2_step = "show"
            st.rerun()

    elif st.session_state.s2_step == "show":
        st.write("### 👁️ 숫자를 잘 기억하세요!")
        st.write(f"현재 맞춰야 할 숫자 개수: **{len(st.session_state.s2_list)}개**")
        
        # 화면에 숫자를 순서대로 보여주고 지우기
        num_container = st.empty()
        for num in st.session_state.s2_list:
            num_container.markdown(f"<h1 style='text-align: center; color: #1f77b4; font-size: 70px;'>{num}</h1>", unsafe_allow_html=True)
            time.sleep(1.2) # 기억할 수 있는 시간 부여
            num_container.empty()
            time.sleep(0.2)
            
        st.session_state.s2_step = "input"
        st.rerun()

    elif st.session_state.s2_step == "input":
        st.write(f"🎮 **라운드 {len(st.session_state.s2_list)}**")
        st.write("보았던 숫자를 **공백(띄어쓰기)으로 구분**하여 순서대로 입력하세요.")
        
        user_str = st.text_input("정답 입력 (예: 7 51 15):", key="s2_input_field")
        
        if st.button("정답 확인 ➡️", key="s2_submit"):
            try:
                # 사용자가 입력한 문자열을 정수 리스트로 변환 (코랩 코드: list(map(int, input().split())))
                user_list = list(map(int, user_str.split()))
                
                if user_list == st.session_state.s2_list:
                    st.success("✨ 맞았다! 다음 단계로 넘어갑니다.")
                    time.sleep(1.0)
                    # 다음 정답 숫자 하나 추가하고 다음 라운드로 이동
                    st.session_state.s2_list.append(random.randint(1, 100))
                    st.session_state.s2_step = "show"
                    st.rerun()
                else:
                    st.error("💀 틀렸다!")
                    st.write(f"입력한 답: {user_list}")
                    st.write(f"실제 정답: {st.session_state.s2_list}")
                    st.markdown(f"### 🏆 최종 점수: **{len(st.session_state.s2_list) - 1}번** 맞췄습니다!")
                    
                    st.session_state.s2_step = "ready"
                    if st.button("처음부터 다시 도전 🔄", key="s2_retry_btn"):
                        st.rerun()
            except ValueError:
                st.warning("숫자만 입력해 주세요! (예: 5 12 77)")


# ==========================================================
# ❤️ 3단계: 라이프 시스템
# ==========================================================
with tab3:
    st.subheader("3단계: 기회가 있는 하트(라이프) 시스템")
    st.info("실수해도 괜찮습니다! 총 3번의 기회가 주어지며, 라이프를 모두 소진할 때까지 얼마나 많이 맞추는지 기록하는 극한의 챌린지 모드입니다.")

    # 3단계 상태 관리 초기화
    if "s3_step" not in st.session_state:
        st.session_state.s3_step = "ready"
    if "s3_list" not in st.session_state:
        st.session_state.s3_list = []
    if "s3_hearts" not in st.session_state:
        st.session_state.s3_hearts = 3 # 기본 하트 개수 H = 3

    if st.session_state.s3_step == "ready":
        if st.button("생존 모드 시작! ❤️", key="s3_start"):
            st.session_state.s3_list = [random.randint(1, 100)]
            st.session_state.s3_hearts = 3
            st.session_state.s3_step = "show"
            st.rerun()

    elif st.session_state.s3_step == "show":
        # 현재 남은 라이프 표시
        st.write(f"### 남은 목숨: {'❤️ ' * st.session_state.s3_hearts}")
        st.write(f"기억해야 할 숫자 개수: **{len(st.session_state.s3_list)}개**")
        
        num_container = st.empty()
        for num in st.session_state.s3_list:
            num_container.markdown(f"<h1 style='text-align: center; color: #2ca02c; font-size: 70px;'>{num}</h1>", unsafe_allow_html=True)
            time.sleep(1.2)
            num_container.empty()
            time.sleep(0.2)
            
        st.session_state.s3_step = "input"
        st.rerun()

    elif st.session_state.s3_step == "input":
        st.write(f"### 남은 목숨: {'❤️ ' * st.session_state.s3_hearts}")
        st.write(f"정답을 띄어쓰기로 구분해서 순서대로 입력하세요.")
        
        user_str3 = st.text_input("정답 입력:", key="s3_input_field")
        
        if st.button("정답 검사 🧪", key="s3_submit"):
            try:
                user_list3 = list(map(int, user_str3.split()))
                
                if user_list3 == st.session_state.s3_list:
                    st.success("✨ 맞았다!")
                    time.sleep(1.0)
                    st.session_state.s3_list.append(random.randint(1, 100))
                    st.session_state.s3_step = "show"
                    st.rerun()
                else:
                    st.error("❌ 틀렸습니다!")
                    st.session_state.s3_hearts -= 1 # 하트 감쇠
                    
                    if st.session_state.s3_hearts <= 0:
                        st.error("💀 게임 오버! 모든 라이프를 소진했습니다.")
                        st.markdown(f"### 🏆 최종 기록: **{len(st.session_state.s3_list) - 1}회** 맞췄습니다!")
                        st.session_state.s3_step = "ready"
                    else:
                        st.warning(f"기회가 {st.session_state.s3_hearts}번 남았습니다. 다시 숫자를 보여드릴게요!")
                        time.sleep(2.0)
                        st.session_state.s3_step = "show"
                    st.rerun()
            except ValueError:
                st.warning("숫자 형식을 정확하게 띄어쓰기로 구분하여 작성해 주세요!")