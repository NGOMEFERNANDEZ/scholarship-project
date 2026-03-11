import streamlit as st

st.set_page_config(
  page_title="HonraAI",
  page_icon="brain",
  layout="wide"
)

with st.sidebar:
  st.title("HONRAAI")
  st.caption("one step at a time")

  st.divider()

  st.subheader("Session Stats")

  col1, col2 = st.columns(2)

  with col1:
   st.metric("Messages", 1)
   
  with col2: 
   st.metric("Total", 1)
   

  st.divider()
  st.subheader("Controls")

  accent = st.selectbox(
    "Accent",
    ["Nigeria", "USA", "UK"]
  )

  temperature = st.slider(
    "Model Temperature",
    0.0, 2.0, 1.2
  )

st.title("Chat with HonraAi")

if "messages" not in st.session_state:
  st.session_state.messages = []

for msg in st.session_state.messages:
  with st.chat_message(msg["role"]):
    st.write(msg["content"])

prompt = st.chat_input("Message HonraAI")
if prompt:

  with st.chat_message("user"):
    st.write(prompt)
  
  st.session_state.messages.append(
    {"role": "user", "content": prompt}
  )

  response = """
Hello There! I'm HonraAI, your friendly and informative assistant specializing in heart disease. I'm here to help you with questions about health, conditions and risk factors.

How can I assist you today?
 """
  
  with st.chat_message("assistant"):
    st.write(response)

    if st.button("Read aloud"):
      st.info("Text-to-speech would play here")

  st.session_state.messages.append(
    {"role": "assistant", "content": response}
  )    
 