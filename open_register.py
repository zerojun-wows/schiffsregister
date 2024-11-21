import streamlit as st
from session_state_routines import is_session_state_empty

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
                "Geöffnetes Schiffsregister wird entfernt und ein leeres Schiffsregister wird eröffnet",
            ],
        )
    # Bei vorhanden Daten sicherheitsabfrage
    # clear session_state
    # set session_state variables
    pass


st.write(st.session_state)
