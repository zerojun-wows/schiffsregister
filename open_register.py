"""
Module contains open or upload part of schiffsregister application
"""
import streamlit as st
from session_state_routines import clear_session_state, is_session_state_empty

st.title("Schiffsregister - Öffnen")

st.write(
    f"Sie können ein neues leeres Schiffsregister eröffnen, oder "
    f"ein bestehendes Schiffsregister hochladen."
)

if st.button("Neues Schiffsregister eröffnen"):
    if not is_session_state_empty:
        st.warning("Ein Schiffsregister ist bereits geöffnet")
        override_request = st.radio(
            "Wollen Sie das bestehende Schiffsregister überschreiben?",
            ["Nein", "Ja"],
            caption=[
                "Es wird kein neues Schiffsregister eröffnet",
                "Geöffnetes Schiffsregister wird entfernt und ein leeres Schiffsregister wird eröffnet",  # noqa: E501
            ],
        )
        if override_request == "Ja":
            # session_state löschen
            # variablen im Session_state setzen
            pass
        else:
            INFO_STR = (
                "Kein neues Schiffsregister eröffnet."
                "Das bereits geöffnete Schiffsregister kann weiterhin genutzt werden."  # noqa: E501
            )
            st.info(
                INFO_STR,
                icon=":material/info:",
            )


st.write(st.session_state)
