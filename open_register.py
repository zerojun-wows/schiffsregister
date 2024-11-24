"""
Module contains open or upload part of schiffsregister application
"""
import streamlit as st
import pandas as pd
from data_config import main_columns
from session_state_routines import (
    clear_session_state,
    is_session_state_empty,
    setup_session_state,
    set_both_ship_registers,
)


def has_uploaded_file_missing_columns(uploaded_file_df: pd.DataFrame) -> bool:
    missing_columns = [
        col for col in main_columns if col not in uploaded_file_df.columns
    ]
    if missing_columns:
        st.error(
            f"Fehlende Spalten: {', '.join(missing_columns)}",
            icon=":material/error:",
        )
        return True
    else:
        return False


def has_uploaded_file_extra_columns(uploaded_file_df: pd.DataFrame) -> bool:
    extra_columns = [col for col in df.columns if col not in main_columns]

    if extra_columns:
        st.warning(
            f"Zusätzliche Spalten: {', '.join(extra_columns)}",
            icon=":material/warning:",
        )
        return True
    else:
        return False


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
    "Bestehende Schiffsregister-Datei auswählen", type="csv"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if not has_uploaded_file_missing_columns(
        df
    ) and not has_uploaded_file_extra_columns(df):
        if not is_session_state_empty():
            pass
        else:
            if st.button("Schiffsregister öffnen"):
                clear_session_state()
                setup_session_state()
                set_both_ship_registers(df)
                st.success(
                    (
                        "Bestehendes Schiffsregister geöffnet. "
                        "Sie können nun zur Ansicht wechseln."
                    ),
                    icon=":material/check_circle:",
                )
                st.page_link(
                    "show_register.py",
                    label="Schiffsregister - Ansehen",
                    icon=":material/news:",
                )


st.write(st.session_state)
