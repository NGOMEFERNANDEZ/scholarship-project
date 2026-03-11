import streamlit as st
from datetime import datetime

# import os


# st.title("Super Simple Title")
# st.header("This is a header")
# st.subheader('Subheader')
# st.markdown("This is _Markdown")
# st.caption("small text")

# code_example = """
# def greet(name)
#     print('hello', name)
# """

# st.code(code_example, language="python")

# st.divider()

# st.image(os.path.join(os.getcwd(), "static", "my_photo.jpg.jpg"))

st.title("User Information")

form_values= {
  "name": None,
  "height": None,
  "gender": None,
  "dob": None
}

min_date = datetime(1990, 1, 1)
max_date = datetime.now()

with st.form(key="user_info_form"):
  form_values["name"] = st.text_input("enter your name: ")
  form_values["age"]  = st.number_input("Enter your age: ")
  form_values["height"] = st.number_input("Enter your height (cm):" )
  form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])
  form_values["dob"] = st.date_input('Enter your birthdate', max_value=max_date, min_value=min_date)
  

  submit_button = st.form_submit_button()
  if submit_button:
    if not all(form_values.values()):
      st.warning("Please Fill in all of the fields")
    else:
      st.balloons()
      st.write("### Info") 
      for (key,value)in form_values.items():
        st.write(f"{key}: {value}")
