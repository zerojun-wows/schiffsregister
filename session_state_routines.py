"""
THis module contains interaction routines with st.session_state 
"""
import pandas as pd
import streamlit as st
from data_config import all_columns


def add_ship_to_current_register(ship_data: dict) -> None:
    st.session_state.ship_register_current.append(ship_data)


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


def clear_remove_index() -> None:
    st.session_state.remove_selected_index = None


def clear_session_state() -> None:
    """
    Removes all keys and values from session_state
    """
    for key in st.session_state.keys():
        del st.session_state[key]


def get_current_ship_register_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        st.session_state.ship_register_current, columns=all_columns
    )


def get_current_ship_register_list() -> list:
    return st.session_state.ship_register_current


def get_original_ship_register_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        st.session_state.ship_register_original, columns=all_columns
    )


def is_form_field_disabled(form_field_name: str) -> bool:
    return st.session_state[f"{form_field_name}_disabled"]


def is_session_state_empty() -> bool:
    return len(st.session_state) == 0


def modify_ship_in_current_register(index: int, ship_data: dict) -> None:
    st.session_state.ship_register_current[index] = ship_data


def reset_add_form() -> None:
    st.session_state.add_ship_nation = None
    st.session_state.add_ship_type = None
    st.session_state.add_ship_class = None
    st.session_state.add_ship_tier = None
    st.session_state.add_ship_name = None


def reset_edit_form() -> None:
    st.session_state.edit_ship_nation = None
    st.session_state.edit_ship_type = None
    st.session_state.edit_ship_class = None
    st.session_state.edit_ship_tier = None
    st.session_state.edit_ship_name = None
    st.session_state.edit_ship_nation_disabled = True
    st.session_state.edit_ship_type_disabled = True
    st.session_state.edit_ship_class_disabled = True
    st.session_state.edit_ship_tier_disabled = True
    st.session_state.edit_ship_name_disabled = True
    st.session_state.edit_form_submit_disabled = True
    st.session_state.edit_form_abort_disabled = True


def set_both_ship_registers(register_df: pd.DataFrame) -> None:
    set_current_ship_register(register_df)
    set_original_ship_register(register_df)


def set_current_ship_register(current_register_df: pd.DataFrame) -> None:
    st.session_state.ship_register_current = current_register_df.to_dict(
        orient="records"
    )


def set_edit_form_values(
    ship_nation: str,
    ship_type: str,
    ship_class: str,
    ship_tier: str,
    ship_name: str,
) -> None:
    st.session_state.edit_ship_nation = ship_nation
    st.session_state.edit_ship_type = ship_type
    st.session_state.edit_ship_class = ship_class
    st.session_state.edit_ship_tier = ship_tier
    st.session_state.edit_ship_name = ship_name


def set_form_field_disabled(form_field_name: str, value: bool) -> None:
    st.session_state[f"{form_field_name}_disabled"] = value


def set_original_ship_register(original_register_df: pd.DataFrame) -> None:
    st.session_state.ship_register_original = original_register_df.to_dict(
        orient="records"
    )


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

    if "register_open_success" not in st.session_state:
        st.session_state.register_open_success = False

    if "edit_ship_nation_disabled" not in st.session_state:
        st.session_state.edit_ship_nation_disabled = True

    if "edit_ship_type_disabled" not in st.session_state:
        st.session_state.edit_ship_type_disabled = True

    if "edit_ship_class_disabled" not in st.session_state:
        st.session_state.edit_ship_class_disabled = True

    if "edit_ship_tier_disabled" not in st.session_state:
        st.session_state.edit_ship_tier_disabled = True

    if "edit_ship_name_disabled" not in st.session_state:
        st.session_state.edit_ship_name_disabled = True

    if "edit_form_submit_enabled" not in st.session_state:
        st.session_state.edit_form_submit_disabled = True

    if "edit_form_abort_enabled" not in st.session_state:
        st.session_state.edit_form_abort_disabled = True

    if "remove_selected_index" not in st.session_state:
        st.session_state.remove_selected_index = None
