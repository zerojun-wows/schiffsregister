import streamlit as st
from data_config import (
    nations_order_dict,
    type_option_list,
    class_order_dict,
    tier_order_dict,
)
from session_state_routines import (
    check_register_open,
    add_ship_to_current_register,
    reset_add_form,
)


st.title("Schiffsregister - Schiff hinzufügen")

check_register_open()

with st.form("add_ship_form"):
    col1, col2 = st.columns(2)

    with col1:
        nation = st.selectbox(
            "Nation",
            options=nations_order_dict.keys(),
            index=None,
            key="add_ship_nation",
            placeholder="Bitte eine Auswahl treffen!",
        )
        typ = st.selectbox(
            "Typ",
            options=type_option_list,
            index=None,
            key="add_ship_type",
            placeholder="Bitte eine Auswahl treffen!",
        )
        klasse = st.selectbox(
            "Klasse",
            options=class_order_dict.keys(),
            index=None,
            key="add_ship_class",
            placeholder="Bitte eine Auswahl treffen!",
        )

    with col2:
        stufe = st.selectbox(
            "Stufe",
            options=tier_order_dict.keys(),
            index=None,
            key="add_ship_tier",
            placeholder="Bitte eine Auswahl treffen!",
        )
        name = st.text_input("Name", key="add_ship_name")

    submitted = st.form_submit_button("Schiff hinzufügen")
    reset = st.form_submit_button("Zurücksetzen", on_click=reset_add_form)

    if all(submitted, not nation, not typ, not klasse, not stufe):
        st.error(
            "In einem der Auswahlfelder fehlt die Auswahl",
            icon=":material/error:",
        )

    if submitted and not name:
        st.error(
            "Der Name des Schiffs darf nicht leer sein!",
            icon=":material/error:",
        )

    if submitted and name:
        add_ship = {
            "Nation": nation,
            "Typ": typ,
            "Klasse": klasse,
            "Stufe": stufe,
            "Name": name,
        }
        add_ship_to_current_register(add_ship)
        st.success(
            f"Das Schiff '{add_ship['Name']}' wurde erfolgreich hinzugefügt!",
            icon=":material/check_circle:",
        )

st.write(st.session_state)
