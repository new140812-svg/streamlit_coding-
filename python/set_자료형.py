import streamlit as st

st.set_page_config(page_title="파이썬 세트 공부방", page_icon="📐")

st.title("📐 세트(Set)를 활용한 삼각형 판별기")
st.write("수업 시간에 필기한 내용을 직접 실행해봅시다!")

st.divider()

# 1. 입력 섹션
st.header("1. 세 각의 크기 입력")
col1, col2, col3 = st.columns(3)

with col1:
    a = st.number_input("각 A", min_value=1, max_value=178, value=60)
with col2:
    b = st.number_input("각 B", min_value=1, max_value=178, value=60)
with col3:
    c = st.number_input("각 C", min_value=1, max_value=178, value=60)

total = a + b + c
st.info(f"현재 세 각의 합: **{total}°**")

# 2. 판별 로직 섹션
st.header("2. 판별 결과")

if total != 180:
    st.error("⚠️ 삼각형이 아닙니다! (세 각의 합이 180도가 되어야 해요)")
else:
    # 필기 내용 핵심: 세트로 변환!
    d = {a, b, c}
    set_length = len(d)
    
    # 시각적 피드백
    st.write(f"생성된 세트 `d` : `{d}`")
    st.write(f"세트의 길이 (`len(d)`) : **{set_length}**")
    
    # 조건문 실행
    if set_length == 1:
        st.success("✨ 결과: **Equilateral (정삼각형)**")
        st.balloons()
    elif set_length == 2:
        st.success("✨ 결과: **Isosceles (이등변삼각형)**")
    else:
        st.success("✨ 결과: **Scalene (부등변삼각형)**")

st.divider()

# 3. 추가 학습 (필기 하단 내용)
st.header("3. 집합 연산 미리보기")
st.code("""
# 리스트 vs 세트 합치기 비교
a_list = [1, 2, 3]
b_list = [3, 4, 5]
# 결과: [1, 2, 3, 3, 4, 5] (중복 포함)

a_set = {1, 2, 3}
b_set = {3, 4, 5}
# 결과 (a_set | b_set): {1, 2, 3, 4, 5} (중복 제거)
""")