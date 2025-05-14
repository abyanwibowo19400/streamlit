import streamlit as st

col1, col2, col3 = st.columns(3)
with col1:

    st.title("Belajar Streamlit 30 Hari by Grok AI")
    st.write("Ini adalah perjalan saya belajar streamlit dibantu oleh Grok AI")
    st.write("Saya mempunyai Hobi untuk belajar hal yang baru, walaupun terkadang saya cepat bosan")
    st.write("saya mengenal streamlit melalui teman asprak alpro saya, yaitu bima")
    st.write("Saya merasa hal ini adalah suatu hal yang baru karena tidak pernah diajarkan pada jurusan saya")

st.columns
with col2:
    tombol = st.button("Tekan") 
    reset = st.button("resset")
    if tombol:
        st.write("Tombol Ditekan")
    else:
        st.write("Tombol Tidak ditekan")