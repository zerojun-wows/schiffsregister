import streamlit as st
import time
from data_config import main_columns
from session_state_routines import (
    check_register_open,
    get_current_ship_register_dataframe,
)

st.title("Schiffsregister - Ausgeben")

check_register_open()

st.subheader("Schiffsregister download")

csv = (
    get_current_ship_register_dataframe()
    .to_csv(columns=main_columns, index=False)
    .encode("utf-8")
)

st.download_button(
    label="Aktuelles Schiffsregister als CSV-Datei herunterladen",
    data=csv,
    file_name=f'{time.strftime("%Y_%m_%d-%H_%M")}-Schiffsregister.csv',
    mime="text/csv",
)
