import streamlit as st

from session_state_routines import (
    check_register_open,
    get_current_ship_register,
)

st.title("Schiffsregister - Ansicht")

check_register_open()

st.subheader("Aktueller Bestand")

current_ship_register_df = get_current_ship_register()

if current_ship_register_df.empty:
    st.info("Noch keine Einträge vorhanden", icon=":material/info:")
else:
    st.dataframe(current_ship_register_df)

st.subheader("Zugänge")

# additions
st.info("Keine Zugänge vorhanden", icon=":material/info:")

st.subheader("Änderungen")

# modifications
st.info("Keine Änderungen vorhanden", icon=":material/info:")

st.subheader("Abgänge")

# removals
st.info("Keine Abgänge vorhanden", icon=":material/info:")

st.write(st.session_state)
