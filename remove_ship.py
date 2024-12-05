import streamlit as st

from session_state_routines import (
    check_register_open,
    get_current_ship_register_list,
)

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
    key="remove_selected_index",
    # on_change=,
    placeholder="Bitte eine Auswahl treffen!",
)

if selected_remove_index is not None and selected_remove_index >= 0:
    selected_ship_data = get_current_ship_register_list()[selected_remove_index]
    st.html(
        "<table width='100%'><tr>"
        "<th>Nation</th><th>Typ</th><th>Klasse</th><th>Stufe</th><th>Name</th>"
        "</tr><tr>"
        f"<td>&emsp;{selected_ship_data['Nation']}</td>"
        f"<td>&emsp;{selected_ship_data['Typ']}</td>"
        f"<td>&emsp;{selected_ship_data['Klasse']}</td>"
        f"<td>&emsp;{selected_ship_data['Stufe']}</td>"
        f"<td>&emsp;{selected_ship_data['Name']}</td>"
    )

    remove_button = st.button("Gewähltes Schiff entfernen")

    if remove_button:
        st.write(
            f"Wollen sie das Schiff {selected_ship_data['Name']} endgültig entfernen?"
        )

# if remove_button and selected_remove_index is None:
#     st.error(
#        "Die Auswahl eines Schiffes ist erforderlich!",
#        icon=":material/error:",
#    )

# if remove_button and (
#    selected_remove_index is not None and selected_remove_index >= 0
# ):
#    selected_ship_data = get_current_ship_register_list()[selected_remove_index]
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
#    remove_confirmation = st.checkbox(
#        f"Bestätige {selected_ship_data['Name']} zu entfernen"
#    )

# remove_request = st.radio(
#    "Wollen Sie dieses Schiff endgültig entfernen?",
#    ["Nein", "Ja"],
#    index=0,
# )
# if remove_request == "Ja" and st.button(
#    f"{selected_ship_data['Name']} endgültig löschen"
# ):
#    pass
