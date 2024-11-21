import streamlit as st
from session_state_routines import check_register_open

st.title("Schiffsregister - Ansicht")

check_register_open()

st.subheader("Aktueller Bestand")

current_ship_register_df = get_current_ship_register_dataframe()

st.write(st.session_state)
