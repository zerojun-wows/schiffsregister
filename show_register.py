import streamlit as st
from session_state_routines import check_register_open

st.title("Schiffsregister - Ansicht")

check_register_open()

st.write(st.session_state)
