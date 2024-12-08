import streamlit as st

from session_state_routines import (
    check_register_open,
    get_current_ship_register_list,
    #    clear_remove_index,
)


def display_ship_information() -> None:
    ship_information_placeholder.write(selected_remove_index)
    # if selected_remove_index is not None and selected_remove_index >= 0:
    #    selected_ship_data = get_current_ship_register_list()[
    #        selected_remove_index
    #    ]
    #    st.html(
    #        "<table width='100%'><tr>"
    #        "<th>Nation</th><th>Typ</th><th>Klasse</th><th>Stufe</th><th>Name</th>"
    #        "</tr><tr>"
    #        f"<td>&emsp;{selected_ship_data['Nation']}</td>"
    #        f"<td>&emsp;{selected_ship_data['Typ']}</td>"
    #        f"<td>&emsp;{selected_ship_data['Klasse']}</td>"
    #        f"<td>&emsp;{selected_ship_data['Stufe']}</td>"
    #        f"<td>&emsp;{selected_ship_data['Name']}</td>"
    #    )


st.title("Schiffsregister - Schiff entfernen")

check_register_open()

if not get_current_ship_register_list():
    st.warning(
        "Es gibt noch keine Einträge, die entfernt werden könnten",
        icon=":material/warning:",
    )
    st.stop()

selected_remove_index = st.selectbox(
    "Auswahl des zu entfernenden Schiffes",
    options=range(len(get_current_ship_register_list())),
    index=None,
    format_func=lambda i: get_current_ship_register_list()[i]["Name"],
    # key="remove_selected_index",
    on_change=display_ship_information,
    placeholder="Bitte eine Auswahl treffen!",
)

ship_information_placeholder = st.empty()

# if selected_remove_index is not None and selected_remove_index >= 0:
# selected_ship_data = get_current_ship_register_list()[selected_remove_index]
# st.html(
#    "<table width='100%'><tr>"
#    "<th>Nation</th><th>Typ</th><th>Klasse</th><th>Stufe</th><th>Name</th>"
#    "</tr><tr>"
#    f"<td>&emsp;{selected_ship_data['Nation']}</td>"
#    f"<td>&emsp;{selected_ship_data['Typ']}</td>"
#    f"<td>&emsp;{selected_ship_data['Klasse']}</td>"
#    f"<td>&emsp;{selected_ship_data['Stufe']}</td>"
#    f"<td>&emsp;{selected_ship_data['Name']}</td>"
# )

#    remove_button = st.button("Gewähltes Schiff entfernen")

#    if remove_button:
#        st.subheader(
#            f"Wollen sie das Schiff {selected_ship_data['Name']}"
#            " endgültig entfernen?"
#        )
#        cols = st.columns(2)
#        abort = cols[0].button(
#            f"Nein, {selected_ship_data['Name']}  nicht entfernen."
#        )
#        confirm = cols[1].button(
#            f"Ja, {selected_ship_data['Name']} engültig entfernen. "
#        )
#       if confirm:
#            st.success(f"Schiff '{selected_ship}' wurde erfolgreich gelöscht!")
#
#        elif abort:
#            st.info("Löschvorgang abgebrochen.")
