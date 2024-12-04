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

selected_remove_index = st.selectbox(
    "Auswahl des zu entfernenden Schiffes",
    options=range(len(get_current_ship_register_list())),
    index=None,
    format_func=lambda i: get_current_ship_register_list()[i]["Name"],
    placeholder="Bitte eine Auswahl treffen!",
)

remove_button = st.button("Gewähltes Schiff entfernen")

if remove_button and selected_remove_index is None:
    st.error(
        "Die Auswahl eines Schiffes ist erforderlich!",
        icon=":material/error:",
    )
