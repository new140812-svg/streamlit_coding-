import streamlit as st

st.title("숫자 나누기 게임")

# 1. 입력 받기
number = st.number_input("숫자를 입력하세요:", min_value=1, step=1)

if st.button("계산 시작"):
    cnt = 0
    temp_number = number # 원본 값을 보존하기 위해 복사
    
    # 2. 반복문 로직
    while temp_number > 1:
        cnt += 1
        temp_number //= 2
        st.write(f"{cnt}번째 단계: {temp_number}")
    
    # 3. 결과 출력
    st.success(f"곱해본 횟수는 {cnt}이다.")