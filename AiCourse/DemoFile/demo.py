
#from PIL import Image
# import pandas as pd

# student_data = {
#  "Name": ["Alice","Bob","Charlie","Dianna"],
 # "Score": [92,78,85,95],
 # "Grade": ["A","C","B","A"]
 # }
# df = pd.DataFrame(student_data)

# st.header("Student Results")
# st.dataframe(df)
# st.table(df)

# image = Image.open("my_photo.jpg.jpg")
# st.image(image, caption="My Profile Photo", use_column_width=True)

# st.video("demo_video.mp4")

# st.audio("audio_file.mp3")



# 

# import streamlit as st

# # Number input box
# age = st.number_input("Enter your age:", min_value=1, max_value=100, value=18)
# st.write("You are", age, "years old.")

# # Slider - great for selecting values in a range
# score = st.slider("Select your exam score:", min_value=0, max_value=100, value=50)

# if score >= 70:
#     st.success("You passed! 🎉")
# elif score >= 50:
#     st.warning("Just passed, keep improving! 💪")
# else:
#     st.error("Below passing mark. Don't give up! 🔥")


# import streamlit as st

# # Dropdown - pick one option
# favourite_language = st.selectbox(
#     "What is your favourite programming language?",
#     ["Python", "JavaScript", "Java", "C++", "Other"]
# )
# st.write("Great choice!", favourite_language, "is a powerful language.")

# # Multiselect - pick multiple options
# modules = st.multiselect(
#     "Which modules are you most excited about?",
#     ["Version Control", "Python", "Streamlit", "FastAPI", "Generative AI", "AI Agents"]
# )

# if modules:
#     st.write("You selected:", ", ".join(modules))

import streamlit as st

# Checkbox - returns True if checked
agree = st.checkbox("I have read and understood the course rules.")

if agree:
    st.success("Thank you! You may proceed.")
else:
    st.warning("Please read and accept the course rules first.")

# Radio - pick one from a visible list
learning_style = st.radio(
    "How do you prefer to learn?",
    ["Watching videos", "Reading notes", "Hands-on practice", "Group discussions"]
)
st.write("We will try to accommodate your style:", learning_style)