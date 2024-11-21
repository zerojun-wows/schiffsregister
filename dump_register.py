import streamlit as st

st.title("Schiffsregister - Ausgeben")

if len(st.session_state) == 0:
    st.info(f"Sie müssen zuerst ein Schiffsregister öffnen.")
    st.page_link("open_register.py", label="Öffnen")
    st.stop()
