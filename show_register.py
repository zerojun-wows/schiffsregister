import streamlit as st
from session_state_routines import check_register_open

st.title("Schiffsregister - Ansicht")

if len(st.session_state) == 0:
    st.info(
        f"Sie müssen zuerst ein Schiffsregister öffnen.",
        icon=":material/info:",
    )
    st.page_link(
        "open_register.py",
        label="Schiffsregister - Öffnen",
        icon=":material/file_open:",
    )
    st.stop()

st.write(st.session_state)
