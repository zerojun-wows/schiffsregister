import streamlit as st
from data_config import (
    nations_order_dict,
    type_option_list,
    class_order_dict,
    tier_order_dict,
)
from session_state_routines import (
    check_register_open,
)

st.title("Schiffsregister - Schiff hinzufügen")

check_register_open()

with st.form("add_ship_form"):
    col1, col2 = st.columns(2)

    with col1:
        nation = st.selectbox(
            "Nation",
            options=nations_order_dict.keys(),
            key="add_ship_nation",
        )
        typ = st.selectbox("Typ", options=type_option_list, key="add_ship_type")
        klasse = st.selectbox(
            "Klasse",
            options=class_order_dict.keys(),
            key="add_ship_class",
        )

    with col2:
        stufe = st.selectbox(
            "Stufe",
            options=tier_order_dict.keys(),
            key="add_ship_tier",
        )
        name = st.text_input("Name", key="add_ship_name")

    submitted = st.form_submit_button("Schiff hinzufügen")

    if submitted and not name:
        st.error(
            "Der Name des Schiffs darf nicht leer sein!",
            icon=":material/error:",
        )

st.write(st.session_state)
