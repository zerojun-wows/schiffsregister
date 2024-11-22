"""
Module contains open or upload part of schiffsregister application
"""
import streamlit as st
from session_state_routines import (
    clear_session_state,
    is_session_state_empty,
    setup_session_state,
    set_register_open_success,
)


st.title("Schiffsregister - Öffnen")

st.write(
    f"Sie können ein neues leeres Schiffsregister eröffnen, oder "
    f"ein bestehendes Schiffsregister hochladen."
)

if st.button("Neues Schiffsregister eröffnen"):
    if not is_session_state_empty():
        st.warning("Ein Schiffsregister ist bereits geöffnet")
        override_request = st.radio(
            "Wollen Sie das bestehende Schiffsregister überschreiben?",
            ["Nein", "Ja"],
            captions=[
                "Es wird kein neues Schiffsregister eröffnet",
                "Geöffnetes Schiffsregister wird entfernt und ein leeres Schiffsregister wird eröffnet",  # noqa: E501
            ],
        )
        if override_request == "Nein":
            set_register_open_success(False)
            INFO_STR = (
                "Kein neues Schiffsregister eröffnet."
                "Das bereits geöffnete Schiffsregister kann weiterhin genutzt werden."  # noqa: E501
            )
            st.info(
                INFO_STR,
                icon=":material/info:",
            )
         else:
            st.write("TEEST")   
    else:
        st.write("Else 1")
        clear_session_state()
        setup_session_state()
        st.success(
            "Neues Schiffsregister eröffnet", icon=":material/check_circle:"
        )

st.write(st.session_state)
st.write(is_session_state_empty())
