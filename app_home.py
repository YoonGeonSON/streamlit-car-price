import streamlit as st

def run_home_app () :
    st.subheader('Welcome')
    st.text('이 입은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('고객 정보를 넣으면, 차 구매 금액도 예측해 줍니다. ')

    st.text('AWS에 배포까지 된 앱입니다.')

    img_url = 'https://image.jtbcplus.kr/data/contents/jam_photo/202007/01/40097b71-7bbe-4de4-9f25-cf04a0b25d66.jpg'
    
    st.image(img_url)