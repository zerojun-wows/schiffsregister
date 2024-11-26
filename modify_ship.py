import streamlit as st

from session_state_routines import (
    check_register_open,
)

st.title("Schiffsregister - Schiff bearbeiten")

check_register_open()
