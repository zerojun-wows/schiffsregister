import streamlit as st

st.title("Schiffsregister - Ausgeben")

if len(st.session_state) == 0:
    st.info("Sie müssen zuerst ein Schiffsregister öffnen.")
