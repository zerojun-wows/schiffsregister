import streamlit as st

from session_state_routines import (
    check_register_open,
    get_current_ship_register_list,
    clear_remove_ship_index,
    set_remove_ship_confirmation,
    get_selected_remove_ship_index,
    set_remove_ship_data,
    get_remove_ship_data,
    is_remove_ship_confirmed,
    remove_ship_from_current_register,
)


def select_ship() -> None:
    set_remove_ship_confirmation(False)
    selected_ship_index = get_selected_remove_ship_index()
    set_remove_ship_data(selected_ship_index)


def confirm_removal() -> None:
    set_remove_ship_confirmation(True)


def update_selectbox() -> None:
    return
    """
    return placeholder_selectbox.selectbox(
        "Auswahl des zu entfernenden Schiffes",
        options=range(len(get_current_ship_register_list())),
        index=None,
        format_func=lambda i: get_current_ship_register_list()[i]["Name"],
        key="selected_remove_ship_index",
        on_change=select_ship,
        placeholder="Bitte eine Auswahl treffen!",
    )"""


st.title("Schiffsregister - Schiff entfernen")

check_register_open()

current_register_list = get_current_ship_register_list()

if not current_register_list:
    st.warning(
        "Es gibt noch keine Einträge, die entfernt werden könnten",
        icon=":material/warning:",
    )
    st.stop()

selected_remove_ship_index = st.selectbox(
    "Auswahl des zu entfernenden Schiffes",
    options=range(len(current_register_list)),
    index=None,
    format_func=lambda i: current_register_list[i]["Name"],
    key="selected_remove_ship_index",
    on_change=select_ship,
    placeholder="Bitte eine Auswahl treffen!",
)

if get_remove_ship_data():
    st.subheader("Details")
    selected_ship_data = get_remove_ship_data()
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

    st.html("<h5>Soll dieses Schiff endgültig entfernt werden?</h5>")
    st.button(
        f"Ja {selected_ship_data['Name']} endgültig löschen",
        on_click=confirm_removal,
    )

    if is_remove_ship_confirmed():
        remove_ship_from_current_register(get_selected_remove_ship_index())
        set_remove_ship_data(None)
        set_remove_ship_confirmation(False)
        clear_remove_ship_index()


st.write(st.session_state)

# if selected_remove_index is not None and selected_remove_index >= 0:
# selected_ship_data = get_current_ship_register_list()[selected_remove_index]

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
