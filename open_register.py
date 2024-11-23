"""
Module contains open or upload part of schiffsregister application
"""
import streamlit as st
from data_config import main_columns
from session_state_routines import (
    clear_session_state,
    is_session_state_empty,
    setup_session_state,
)


st.title("Schiffsregister - Öffnen")

st.write(
    f"Sie können ein neues leeres Schiffsregister eröffnen, oder "
    f"ein bestehendes Schiffsregister hochladen."
)

if not is_session_state_empty():
    st.warning("Ein Schiffsregister ist bereits geöffnet")

st.subheader("Neues Schiffsregister")

if not is_session_state_empty():
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
                (
                    "Neues Schiffsregister eröffnet."
                    "Sie können nun zur Ansicht wechseln."
                ),
                icon=":material/check_circle:",
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
            (
                "Neues Schiffsregister eröffnet. "
                "Sie können nun zur Ansicht wechseln."
            ),
            icon=":material/check_circle:",
        )
        st.page_link(
            "show_register.py",
            label="Schiffsregister - Ansehen",
            icon=":material/news:",
        )

st.subheader("Schiffsregister hochladen")

uploaded_file = st.file_uploader(
    "Bestehendes Schiffsregister hochladen", type="csv"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if not is_session_state_empty():
        pass
    else:
        pass


st.write(st.session_state)
