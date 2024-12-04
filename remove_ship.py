import streamlit as st

from session_state_routines import (
    check_register_open,
)

st.title("Schiffsregister - Schiff entfernen")

check_register_open()

if not get_current_ship_register_list():
    st.warning(
        "Es gibt noch keine Einträge, die entfernt werden könnten",
        icon=":material/warning:",
    )
    st.stop()
