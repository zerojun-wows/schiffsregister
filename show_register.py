import streamlit as st

from session_state_routines import (
    check_register_open,
    get_current_ship_register_dataframe,
    get_additions_dataframe,
    get_modifications_dataframe,
)

st.title("Schiffsregister - Ansicht")

check_register_open()

st.subheader("Aktueller Bestand")

current_ship_register_df = get_current_ship_register_dataframe()

if current_ship_register_df.empty:
    st.info("Noch keine Einträge vorhanden", icon=":material/info:")
else:
    st.dataframe(current_ship_register_df)

st.subheader("Zugänge")

# additions
if current_ship_register_df.empty:
    st.info("Keine Zugänge vorhanden", icon=":material/info:")
else:
    st.dataframe(get_additions_dataframe())

st.subheader("Änderungen")

# get_modifications_dataframe
if current_ship_register_df.empty:
    st.info("Keine Änderungen vorhanden", icon=":material/info:")
else:
    st.dataframe(get_modifications_dataframe())

st.subheader("Abgänge")

# removals
st.info("Keine Abgänge vorhanden", icon=":material/info:")

st.write(st.session_state)
