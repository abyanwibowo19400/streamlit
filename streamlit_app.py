import streamlit as st

st.title("Program Streamlit 30 Hari Bersama Grok AI")

col1, col2, col3 = st.columns([2,2,3])

col1.subheader("Ini adalah Subheader dari kolom 1")
with col1:
    st.write("Ini adalah kolom 1")

col2.subheader("Ini adalah Subheader dari kolom 2")
with col2:
    st.write("Ini adalah kolom 2")

col3.subheader("Ini adalah Subheader dari kolom 3")
with col3:
    st.write("Ini adalah kolom 3")