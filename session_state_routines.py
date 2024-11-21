"""
THis module contains interaction routines with st.session_state 
"""
import streamlit as st


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


def clear_session_state() -> None:
    for key in st.session_state.keys():
        del st.session_state[key]


def is_session_state_empty() -> bool:
    if len(st.is_session_state_empty) == 0:
        return True
    return False


def setup_session_state() -> None:
    pass
