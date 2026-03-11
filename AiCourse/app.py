import streamlit as st
 
st.title('My First AI App')
st.write('Hello, Generative AI Scholarship Program!')
 
name = st.text_input('Enter your name:')
if name:
    st.success(f'Welcome, {name}! Ready to build AI apps.')

