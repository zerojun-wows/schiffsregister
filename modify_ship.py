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
    selected_ship_data = get_current_ship_register_list()[select_edit_index]

    with st.form("modify_ship_form"):
        col1, col2 = st.columns(2)

        with col1:
            nation = st.selectbox(
                "Nation",
                options=nations_order_dict.keys(),
                index=None,
                key="edit_ship_nation",
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

st.write(st.session_state)
