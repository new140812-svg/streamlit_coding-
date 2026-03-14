import streamlit as st
import time
import pandas as pd
import numpy as np

st.set_page_config(page_title="알고리즘 효율성 실험실", page_icon="⏱️")

st.title("⏱️ 알고리즘: 누가 더 빠를까?")
st.write("똑같은 결과를 내더라도 방법(알고리즘)에 따라 성능은 천차만별입니다.")

# 1. 입력 섹션
n = st.slider("데이터의 양 (n)을 조절해보세요", min_value=1, max_value=500, value=100)

st.divider()

# 2. 알고리즘 실행 및 시각화
st.header(f"1부터 {n}까지 합치기 대결")

# 데이터 준비용 리스트
results = []

# --- 전략 1: 천재적 알고리즘 O(1) ---
start_1 = time.perf_counter()
total_1 = n * (n + 1) // 2
end_1 = time.perf_counter()
time_1 = end_1 - start_1

# --- 전략 2: 뚜벅이 알고리즘 O(n) ---
start_2 = time.perf_counter()
total_2 = 0
for i in range(1, n + 1):
    total_2 += i
end_2 = time.perf_counter()
time_2 = end_2 - start_2

# --- 전략 3: 거북이 알고리즘 O(n^2) ---
start_3 = time.perf_counter()
total_3 = 0
for i in range(1, n + 1):
    for j in range(i):
        total_3 += 1
end_3 = time.perf_counter()
time_3 = end_3 - start_3

# 결과 카드 출력
col1, col2, col3 = st.columns(3)
col1.metric("천재형 O(1)", f"{total_1}", f"{time_1:.6f}s")
col2.metric("뚜벅이 O(n)", f"{total_2}", f"{time_2:.6f}s")
col3.metric("거북이 O(n^2)", f"{total_3}", f"{time_3:.6f}s")

st.divider()

# 3. 그래프로 보는 연산 횟수의 차이
st.header("📈 연산 횟수 시각화 (Big-O)")

# 데이터프레임 생성
x = np.arange(1, n + 1)
df = pd.DataFrame({
    'n (데이터 개수)': x,
    'O(1) - 상수': [1] * n,
    'O(n) - 선형': x,
    'O(n^2) - 제곱': x**2
})

st.line_chart(df, x='n (데이터 개수)', y=['O(1) - 상수', 'O(n) - 선형', 'O(n^2) - 제곱'])

st.warning(f"보이시나요? n이 {n}일 때, 거북이 알고리즘(n^2)은 벌써 그래프 천장을 뚫고 나가려 합니다!")

st.info("""
**💡 광희님의 필기 포인트 정리:**
- **O(1)**: 데이터가 아무리 많아도 속도가 일정함 (가장 좋음)
- **O(n)**: 데이터 양만큼 시간이 늘어남 (무난함)
- **O(n^2)**: 데이터가 조금만 많아져도 시간이 폭발적으로 늘어남 (주의 필요!)
""")