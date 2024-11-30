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
    is_form_field_disabled,
    set_form_field_disabled,
    modify_ship_in_current_register,
)


def get_missing_fields(_nation, _typ, _klasse, _stufe) -> list[str]:
    fehlende_felder = []
    if not _nation:
        fehlende_felder.append("Nation")
    if not _typ:
        fehlende_felder.append("Typ")
    if not _klasse:
        fehlende_felder.append("Klasse")
    if not _stufe:
        fehlende_felder.append("Stufe")
    return fehlende_felder


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
    set_form_field_disabled("edit_ship_nation", False)
    set_form_field_disabled("edit_ship_type", False)
    set_form_field_disabled("edit_ship_class", False)
    set_form_field_disabled("edit_ship_tier", False)
    set_form_field_disabled("edit_ship_name", False)
    set_form_field_disabled("edit_form_submit", False)
    set_form_field_disabled("edit_form_abort", False)


with st.form("modify_ship_form"):
    col1, col2 = st.columns(2)

    with col1:
        nation = st.selectbox(
            "Nation",
            options=nations_order_dict.keys(),
            index=None,
            key="edit_ship_nation",
            placeholder="Bitte eine Auswahl treffen!",
            disabled=is_form_field_disabled("edit_ship_nation"),
        )
        typ = st.selectbox(
            "Typ",
            options=type_option_list,
            index=None,
            key="edit_ship_type",
            placeholder="Bitte eine Auswahl treffen!",
            disabled=is_form_field_disabled("edit_ship_type"),
        )
        klasse = st.selectbox(
            "Klasse",
            options=class_order_dict.keys(),
            index=None,
            key="edit_ship_class",
            placeholder="Bitte eine Auswahl treffen!",
            disabled=is_form_field_disabled("edit_ship_class"),
        )

    with col2:
        stufe = st.selectbox(
            "Stufe",
            options=tier_order_dict.keys(),
            index=None,
            key="edit_ship_tier",
            placeholder="Bitte eine Auswahl treffen!",
            disabled=is_form_field_disabled("edit_ship_tier"),
        )
        name = st.text_input(
            "Name",
            key="edit_ship_name",
            disabled=is_form_field_disabled("edit_ship_name"),
        )

    col3, col4 = st.columns(2)

    with col3:
        submitted = st.form_submit_button(
            "Änderungen übernehmen",
            disabled=is_form_field_disabled("edit_form_submit"),
        )

    with col4:
        reset = st.form_submit_button(
            "Bearbeitung abbrechen",
            on_click=reset_edit_form,
            disabled=is_form_field_disabled("edit_form_abort"),
        )

    if submitted and any([not nation, not typ, not klasse, not stufe]):
        st.error(
            (
                "Bitte treffen Sie bei den folgenden Feldern eine Auswahl: "
                f"{', '.join(get_missing_fields(nation, typ, klasse, stufe))}"
            ),
            icon=":material/error:",
        )

    if submitted and not name.strip():
        st.error(
            "Der Name des Schiffs darf nicht leer sein!",
            icon=":material/error:",
        )

    if all([submitted, name.strip(), nation, typ, klasse, stufe]):
        ship_data = {
            "Nation": nation,
            "Typ": typ,
            "Klasse": klasse,
            "Stufe": stufe,
            "Name": name,
        }

        st.success(
            f"Das Schiff '{selected_ship_data['Name']}' wurde erfolgreich geändert!",
            icon=":material/check_circle:",
        )

st.write(st.session_state)
