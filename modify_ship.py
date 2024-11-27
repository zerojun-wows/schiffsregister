import streamlit as st

from session_state_routines import (
    check_register_open,
)

st.title("Schiffsregister - Schiff bearbeiten")

check_register_open()

# select_edit_index = st.selectbox("Auswahl des zu bearbeitenden Schiffes",)

st.write(st.session_state)

st.write(type(st.session_state.ship_register_current))
