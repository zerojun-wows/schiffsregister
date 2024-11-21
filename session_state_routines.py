import streamlit as st


def is_session_state_empty() -> bool:
    if len(st.is_session_state_empty) == 0:
        return True
    return False


def check_register_open() -> None:
    if is_session_state_empty:
        st.info(
            "Sie müssen zuerst ein Schiffsregister öffnen.",
            icon=":material/info:",
        )
        st.page_link(
            "open_register.py",
            label="Schiffsregister - Öffnen",
            icon=":material/file_open:",
        )
        st.stop()
