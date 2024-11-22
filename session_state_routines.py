"""
THis module contains interaction routines with st.session_state 
"""
import pandas as pd
import streamlit as st
from data_config import all_columns


def check_register_open() -> None:
    if is_session_state_empty():
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
    """
    Removes all keys and values from session_state
    """
    for key in st.session_state.items():
        del st.session_state[key]


def get_current_ship_register_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        st.session_state.ship_register_current, columns=all_columns
    )


def get_original_ship_register_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        st.session_state.ship_register_original, columns=all_columns
    )


def is_session_state_empty() -> bool:
    if len(st.session_state) == 0:
        return True
    return False


def setup_session_state() -> None:
    if "ship_register_original" not in st.session_state:
        st.session_state.ship_register_original = []

    if "ship_register_current" not in st.session_state:
        st.session_state.ship_register_current = []

    if "additions_id_list" not in st.session_state:
        st.session_state.additions_ids = []

    if "modifications_id_list" not in st.session_state:
        st.session_state.modifacions_id_list = []

    if "removals_id_list" not in st.session_state:
        st.session_state.removals_id_list = []
