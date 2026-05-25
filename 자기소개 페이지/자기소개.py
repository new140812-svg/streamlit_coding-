import streamlit as st

# 페이지 설정 (브라우저 탭 이름과 아이콘)
st.set_page_config(page_title="김광희의 프로필", page_icon="💻", layout="centered")

# --- 프로필 버전 관리를 위한 세션 상태 초기화 ---
if "profile_version" not in st.session_state:
    st.session_state.profile_version = "new"  # 기본값은 새로운 코딩 중심 프로필

# 버전을 전환하는 함수
def switch_version():
    if st.session_state.profile_version == "new":
        st.session_state.profile_version = "old"
    else:
        st.session_state.profile_version = "new"

# ==========================================================
# 1. 새로운 버전 (코딩 중심 프로필)
# ==========================================================
if st.session_state.profile_version == "new":
    # --- 헤더 및 소개 ---
    st.title("💻 안녕하세요, 개발자 김광희입니다!")
    st.subheader("알고리즘과 파이썬 코딩을 사랑하는 개발자의 성장 기록")

    # --- 프로필 카드 레이아웃 ---
    st.markdown("---")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("<h1 style='text-align: center; font-size: 80px;'>👨‍💻</h1>", unsafe_allow_html=True) 
        st.markdown("<p style='text-align: center; font-weight: bold; font-size: 20px;'>김광희 (Kwanghee)</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("### 🔍 **Profile**")
        st.markdown("""
        * 🧬 **정체성:** 끊임없이 문제를 해결하는 **개발자**
        * 🛠️ **주요 무기:** 파이썬(Python) & 알고리즘 트레이닝
        * 🎯 **목표:** 코딩에서 훌륭한 인재되기!
        """)

    st.divider()

    # --- 알고리즘 실력 및 백준 배지 (가장 강조!) ---
    st.header("🏆 백준 알고리즘 실력")
    st.write("문제를 풀며 매일 성장하고 있는 저의 백준(BOJ) Solved 배지입니다. 클릭하면 제 프로필로 이동합니다!")

    # 배지를 중앙에 이쁘게 정렬하기 위한 레이아웃
    badge_col1, badge_col2 = st.columns([2, 3])

    with badge_col1:
        st.markdown(
            """ 
            <div style="text-align: center; background-color: #f0f2f6; padding: 15px; border-radius: 10px; border: 1px solid #ddd;">
                <a href="https://solved.ac/new140812/" target="_blank">
                    <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=new140812" style="max-width: 100%; height: auto;" />
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with badge_col2:
        st.markdown("### **solved.ac 분석**")
        st.write("✔️ **해결 능력:** 수학적 사고 and 조건문 구현에 강함")
        st.write("✔️ **트레이닝 분야:** 자료구조, 수학, 구현, 정렬")
        st.write("✔️ **현재 목표:** 매주 3개 이상의 실버/골드 난이도 문제 정복")

    st.divider()

    # --- 코딩 및 기술 능력치 ---
    st.header("📊 기술 스택 & 능력치")

    st.write("🐍 **Python (파이썬)**")
    st.progress(75)
    st.caption("클래스, 함수 및 기초 자료형을 능숙하게 다루며 웹 스크래핑 및 자동화 도구를 빌드할 수 있습니다.")

    st.write("📊 **Streamlit (대시보드 앱 구현)**")
    st.progress(60)
    st.caption("파이썬 파일 하나로 프로토타입 웹 애플리케이션을 신속하게 개발하고 배포할 수 있습니다.")

    st.write("🧠 **Algorithm & Data Structure (알고리즘 및 자료구조)**")
    st.progress(50)
    st.caption("시간 복잡도를 고려한 정렬, 탐색 및 기본 조건/반복문 구현에 강점이 있습니다.")

    st.divider()

    # --- 방명록 서비스 ---
    st.subheader("💬 동료 개발자에게 한마디")
    guest_book = st.text_input("방문 기념 응원 메시지나 코드 피드백을 남겨주세요!", key="guest_new")
    if st.button("등록하기", key="btn_guest_new"):
        if guest_book:
            st.toast(f"👍 '{guest_book}' 메시지가 정상 등록되었습니다. 감사합니다!", icon="🔥")
        else:
            st.warning("내용을 입력한 뒤 등록 버튼을 눌러주세요!")


# ==========================================================
# 2. 이전 버전 (게임 섹션이 포함된 오리지널 프로필)
# ==========================================================
else:
    # --- 헤더 및 소개 ---
    st.title("안녕하세요, 김광희입니다! 👋")
    st.subheader("배움과 놀기를 좋아하는 사람의 성장 기록")

    # --- 프로필 카드 레이아웃 ---
    st.markdown("---")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("<h1 style='text-align: center; font-size: 80px;'>👨‍💻</h1>", unsafe_allow_html=True) 
        st.markdown("<p style='text-align: center; font-weight: bold; font-size: 20px;'>김광희</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("### 🔍 **Who am I?**")
        st.markdown("""
        * 🧬 **정체성:** 아주 평범하고 유쾌한 **사람임**
        * 🎮 **취미:** 신나게 **놀기** & 맛있는 것 먹기
        * 🎯 **관심사:** 요즘 파이썬이랑 스트림릿으로 이것저것 만들어보는 재미에 푹 빠짐!
        """)

    # --- 능력치 그래프 ---
    st.markdown("### 📊 나의 능력치 수치")
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.write("🎮 놀기 능력")
        st.progress(99) # 99% 놀기 장인
    with col_stat2:
        st.write("💻 파이썬 코딩")
        st.progress(65) # 열심히 성장 중!

    st.divider()

    # --- 취미 섹션 ---
    st.header("🎮 My Hobby: Gaming")
    st.info("저는 게임을 통해 전략을 짜고 새로운 세계를 탐험하는 것을 즐깁니다.")

    game_genre = st.selectbox(
        "광희님이 가장 좋아하는 게임 장르는?",
        ("RPG", "FPS", "시뮬레이션", "스포츠", "인디 게임")
    )
    st.write(f"아하! **{game_genre}** 장르를 좋아하시는군요! 저랑 취향이 비슷하신데요? 😉")

    st.divider()

    # --- 알고리즘 실력 섹션 ---
    st.header("🏆 나의 코딩 실력 (백준)")
    st.write("백준(BOJ) 문제를 풀며 다져진 굳건한 솔브드 실력 배지입니다!")

    badge_col1, badge_col2 = st.columns([1, 3])
    with badge_col1:
        st.markdown(
            """ 
            <a href="https://solved.ac/new140812/">
                <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=new140812" width="180"/>
            </a>
            """,
            unsafe_allow_html=True
        )
    with badge_col2:
        st.success("🔥 끈기 있게 알고리즘 문제를 풀어내고 있는 든든한 증표입니다!")

    st.divider()

    # --- 방명록 서비스 ---
    st.subheader("💬 응원 한마디 남기기")
    guest_book = st.text_input("김광희에게 응원의 한마디를 적어주세요!", key="guest_old")
    if st.button("등록하기", key="btn_guest_old"):
        if guest_book:
            st.toast(f"👍 '{guest_book}' 메시지가 등록되었습니다! 응원 감사합니다!", icon="😍")
        else:
            st.warning("내용을 입력하고 버튼을 눌러주세요!")


# --- 하단 푸터 ---
st.divider()
st.caption("© 2026. 김광희 All rights reserved.")


# ==========================================================
# 🔄 3. 프로필 실시간 전환 버튼 (사용자가 요청한 핵심 기능!)
# ==========================================================
st.write("### 🔄 프로필 테마 변경")
if st.session_state.profile_version == "new":
    st.info("현재 화면: **코딩 중심 프로필**")
    if st.button("🎮 옛날 프로필 화면으로 바꾸기!"):
        switch_version()
        st.rerun()
else:
    st.info("현재 화면: **이전 프로필(게임 테마)**")
    if st.button("💻 새로운 프로필(코딩 중심)로 화면 바꾸기"):
        switch_version()
        st.rerun()


# ==========================================================
# 📦 4. 이전 코드 아카이브 (접고 펼칠 수 있는 소스 코드 보관소)
# ==========================================================
st.write("")
st.write("")
with st.expander("📦 [보관소] 이전 버전의 자기소개 소스 코드 보기 (게임 내용 포함)"):
    st.info("이전에 작성했던 게임 선택 인터랙티브 기능이 포함된 순수 파이썬 소스 코드입니다.")
    st.code("""
import streamlit as st

# 페이지 설정 (브라우저 탭 이름과 아이콘)
st.set_page_config(page_title="김광희의 프로필", page_icon="👋", layout="centered")

# --- 헤더 및 소개 ---
st.title("안녕하세요, 김광희입니다! 👋")
st.subheader("배움과 놀기를 좋아하는 사람의 성장 기록")

# --- 프로필 카드 레이아웃 ---
st.markdown("---")
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>👨‍💻</h1>", unsafe_allow_html=True) 
    st.markdown("<p style='text-align: center; font-weight: bold;'>김광희</p>", unsafe_allow_html=True)

with col2:
    st.markdown("### 🔍 **Who am I?**")
    st.markdown(\"\"\"
    * 🧬 **정체성:** 아주 평범하고 유쾌한 **사람임**
    * 🎮 **취미:** 신나게 **놀기** & 맛있는 것 먹기
    * 🎯 **관심사:** 요즘 파이썬이랑 스트림릿으로 이것저것 만들어보는 재미에 푹 빠짐!
    \"\"\")

# --- 능력치 그래프 ---
st.markdown("### 📊 나의 능력치 수치")
col_stat1, col_stat2 = st.columns(2)
with col_stat1:
    st.write("🎮 놀기 능력")
    st.progress(99)
with col_stat2:
    st.write("💻 파이썬 코딩")
    st.progress(65)

st.divider()

# --- 취미 섹션 ---
st.header("🎮 My Hobby: Gaming")
st.info("저는 게임을 통해 전략을 짜고 새로운 세계를 탐험하는 것을 즐깁니다.")

game_genre = st.selectbox(
    "광희님이 가장 좋아하는 게임 장르는?",
    ("RPG", "FPS", "시뮬레이션", "스포츠", "인디 게임")
)

st.write(f"아하! **{game_genre}** 장르를 좋아하시는군요! 저랑 취향이 비슷하신데요? 😉")

st.divider()

# --- 알고리즘 실력 섹션 ---
st.header("🏆 나의 코딩 실력 (백준)")
st.write("백준(BOJ) 문제를 풀며 다져진 굳건한 솔브드 실력 배지입니다!")

badge_col1, badge_col2 = st.columns([1, 3])
with badge_col1:
    st.markdown(
        \"\"\" 
        <a href="https://solved.ac/new140812/">
            <img src="http://mazassumnida.wtf/api/v2/generate_badge?boj=new140812" width="180"/>
        </a>
        \"\"\",
        unsafe_allow_html=True
    )
with badge_col2:
    st.success("🔥 끈기 있게 알고리즘 문제를 풀어내고 있는 든든한 증표입니다!")
    """, language="python")