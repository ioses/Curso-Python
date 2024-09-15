import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Iñigo Osés")
    content ="""
    Hola soy Iñigo Osés y esto es una prueba para un curso de Python
    """
    st.write(content)


content2="""
    Below you can find some of the apps I have built in Python. Please, feel free to check them and if you like it please tell me
    """
st.write(content2)