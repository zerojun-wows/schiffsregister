"""
Module contains open or upload part of schiffsregister application
"""
import streamlit as st
from session_state_routines import (
    clear_session_state,
    is_session_state_empty,
    setup_session_state,
    is_register_open_success,
    set_register_open_success,
)


st.title("Schiffsregister - Öffnen")

st.write(
    f"Sie können ein neues leeres Schiffsregister eröffnen, oder "
    f"ein bestehendes Schiffsregister hochladen."
)

if not is_session_state_empty():
    st.warning("Ein Schiffsregister ist bereits geöffnet")
    override_request = st.radio(
        "Wollen Sie das bestehende Schiffsregister überschreiben?",
        ["Nein", "Ja"],
        index=0,
        captions=[
            "Es wird kein neues Schiffsregister eröffnet",
            "Geöffnetes Schiffsregister wird entfernt und ein leeres Schiffsregister wird eröffnet",  # noqa: E501
        ],
    )
    if override_request == "Ja":
        if st.button("Schiffregister entfernen und Neues eröffnen"):
            clear_session_state()
            setup_session_state()
            st.success(
                "Neues Schiffsregister eröffnet", icon=":material/check_circle:"
            )
            st.page_link(
                "show_register.py",
                label="Schiffsregister - Ansehen",
                icon=":material/news:",
            )
else:
    if st.button("Neues Schiffsregister eröffnen"):
        clear_session_state()
        setup_session_state()
        st.success(
            "Neues Schiffsregister eröffnet. "
            "Sie können nun zur Ansicht wechseln.",
            icon=":material/check_circle:",
        )

st.write(st.session_state)
