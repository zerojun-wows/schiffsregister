import streamlit as st

from session_state_routines import (
    check_register_open,
    get_current_ship_register_list,
)


st.title("Schiffsregister - Schiff bearbeiten")

check_register_open()

if not get_current_ship_register_list():
    st.warning(
        "Es gibt noch keine Einträge, die bearbeitet werden könnten",
        icon=":material/warning:",
    )
    st.stop()

select_edit_index = st.selectbox(
    "Auswahl des zu bearbeitenden Schiffes",
    options=range(len(get_current_ship_register_list())),
    format_func=lambda i: get_current_ship_register_list()[i]["Name"],
)

if st.button("Gewähltes Schiff bearbeiten"):
    entry = get_current_ship_register_list()[select_edit_index]

    st.write(entry)


st.write(st.session_state)
