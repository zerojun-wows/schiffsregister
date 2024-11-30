import streamlit as st
from data_config import (
    nations_order_dict,
    type_option_list,
    class_order_dict,
    tier_order_dict,
)
from session_state_routines import (
    check_register_open,
    get_current_ship_register_list,
    reset_edit_form,
    set_edit_form_values,
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
    index=None,
    placeholder="Bitte eine Auswahl treffen!",
)

if st.button("Gewähltes Schiff bearbeiten"):
    selected_ship_data = get_current_ship_register_list()[select_edit_index]
    set_edit_form_values(
        selected_ship_data["Nation"],
        selected_ship_data["Typ"],
        selected_ship_data["Klasse"],
        selected_ship_data["Stufe"],
        selected_ship_data["Name"],
    )
    # st.write(selected_ship_data)

with st.form("modify_ship_form"):
    col1, col2 = st.columns(2)

    with col1:
        nation = st.selectbox(
            "Nation",
            options=nations_order_dict.keys(),
            # index=nations_order_dict[selected_ship_data["Nation"]] - 1
            # if selected_ship_data
            # else None,
            key="edit_ship_nation",
            placeholder="Bitte eine Auswahl treffen!",
        )
        typ = st.selectbox(
            "Typ",
            options=type_option_list,
            # index=type_option_list.index(selected_ship_data["Typ"])
            # if selected_ship_data
            # else None,
            key="edit_ship_type",
            placeholder="Bitte eine Auswahl treffen!",
        )
        klasse = st.selectbox(
            "Klasse",
            options=class_order_dict.keys(),
            # index=class_order_dict[selected_ship_data["Klasse"]] - 1
            # if selected_ship_data
            # else None,
            key="edit_ship_class",
            placeholder="Bitte eine Auswahl treffen!",
        )

    with col2:
        stufe = st.selectbox(
            "Stufe",
            options=tier_order_dict.keys(),
            # index=tier_order_dict[selected_ship_data["Stufe"]]
            # if selected_ship_data
            # else None,
            key="edit_ship_tier",
            placeholder="Bitte eine Auswahl treffen!",
        )
        name = st.text_input(
            "Name",
            # value=selected_ship_data["Name"],
            key="edit_ship_name",
        )

    col3, col4 = st.columns(2)

    with col3:
        submitted = st.form_submit_button("Änderungen übernehmen")

    with col4:
        reset = st.form_submit_button(
            "Bearbeitung abbrechen", on_click=reset_edit_form
        )

    if submitted and not name:
        st.error(
            "Der Name des Schiffs darf nicht leer sein!",
            icon=":material/error:",
        )


st.write(st.session_state)
