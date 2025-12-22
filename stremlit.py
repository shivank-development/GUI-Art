import streamlit as st

st.title("Hello Frontend in Python 👋")
name = st.text_input("Enter your name:")
st.write(f"Welcome, {name}!")
if st.button("Click Me"):
    st.write("Button clicked!")
elif st.button("Another Button"):
    st.write("Another button clicked!")
    st.balloons()
elif st.checkbox("Check me"):
    st.write("Checkbox is checked!")
    st.image("https://picsum.photos/200/300", caption="Random Image")
else:
    st.write("Checkbox is not checked!")
st.write("This is a simple Streamlit app.")

