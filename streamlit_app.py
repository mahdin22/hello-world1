import streamlit as st

st.title("🎈 HELLO WORLD")

name = st.text_input("name ;")

if(name):
    st("hello", name)
else:
    st.warning("isi nama mahdin")
    
st.write(
    name
)
