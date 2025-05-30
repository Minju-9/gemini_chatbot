import streamlit as st
import google.generativeai as genai

# 페이지 설정
st.set_page_config(
    page_title="Gemini 챗봇",
    page_icon="🤖"
)

# Gemini API 키 설정
genai.configure(api_key=st.secrets["gemini"]["api_key"])

# 모델 설정
model = genai.GenerativeModel('gemini-1.5-flash')

# 세션 상태 초기화
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# 제목 표시
st.title("🤖 Gemini 챗봇")

# 채팅 히스토리 표시
for message in st.session_state.chat.history:
    if message.role == "user":
        st.chat_message("user").write(message.parts[0].text)
    else:
        st.chat_message("assistant").write(message.parts[0].text)

# 사용자 입력 처리
if prompt := st.chat_input("메시지를 입력하세요"):
    # 사용자 메시지 표시
    st.chat_message("user").write(prompt)
    
    try:
        # Gemini로 응답 생성
        response = st.session_state.chat.send_message(prompt)
        
        # 어시스턴트 응답 표시
        st.chat_message("assistant").write(response.text)
    
    except Exception as e:
        st.error(f"오류가 발생했습니다: {str(e)}")
