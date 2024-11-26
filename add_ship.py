import streamlit as st
from data_config import (
    nations_order_dict,
    type_option_list,
)
from session_state_routines import (
    check_register_open,
)

st.title("Schiffsregister - Schiff hinzufügen")

check_register_open()

with st.form("add_ship_form"):
    nation = st.selectbox(
        "Nation",
        options=nations_order_dict.keys(),
        key="add_ship_nation",
    )
    typ = st.selectbox("Typ", options=type_option_list, key="add_ship_type")
    klasse = st.selectbox(
        "Klasse",
        options=ship_class_order_dict.keys(),
        key="add_ship_class",
    )

    submitted = st.form_submit_button("Schiff hinzufügen")
