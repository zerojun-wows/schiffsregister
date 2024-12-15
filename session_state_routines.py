"""
This module contains interaction routines with st.session_state
"""
import pandas as pd
import streamlit as st
from data_config import (
    all_columns,
    nations_order_dict,
    class_order_dict,
    tier_order_dict,
    sort_field_order,
)


def add_ship_to_current_register(ship_data: dict) -> None:
    st.session_state.ship_register_current.append(ship_data)


def calculate_order_values(df) -> None:
    df["Ordnungswert_Nation"] = df["Nation"].map(nations_order_dict)
    df["Ordnungswert_Klasse"] = df["Klasse"].map(class_order_dict)
    df["Ordnungswert_Stufe"] = df["Stufe"].map(tier_order_dict)


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


def clear_remove_ship_index() -> None:
    st.session_state.remove_selected_ship_index = None


def clear_session_state() -> None:
    """
    Removes all keys and values from session_state
    """
    for key in st.session_state.keys():
        del st.session_state[key]


def get_additions_dataframe() -> pd.DataFrame:
    original_register_df = get_original_ship_register_dataframe()
    current_register_df = get_current_ship_register_dataframe()

    new_indices = current_register_df.index.difference(
        original_register_df.index
    )

    return current_register_df.loc[new_indices]


def get_current_ship_register_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        st.session_state.ship_register_current, columns=all_columns
    )


def get_current_ship_register_list() -> list:
    return st.session_state.ship_register_current


def get_modifications_dataframe() -> pd.DataFrame:
    original_register_df = get_original_ship_register_dataframe()
    current_register_df = get_current_ship_register_dataframe()

    common_indices = original_register_df.index.intersection(
        current_register_df.index
    )

    if not original_register_df.empty and not current_register_df.empty:
        original_subset = original_register_df.loc[common_indices]
        current_subset = current_register_df.loc[common_indices]

        return original_subset.compare(current_subset)
    else:
        return original_register_df


def get_original_ship_register_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        st.session_state.ship_register_original, columns=all_columns
    )


def get_removals_dataframe() -> pd.DataFrame:
    original_register_df = get_original_ship_register_dataframe()
    current_register_df = get_current_ship_register_dataframe()

    deleted_indices = original_register_df.index.difference(
        current_register_df.index
    )
    return original_register_df.loc[deleted_indices]


def get_remove_ship_data():
    return st.session_state.remove_ship_data


def get_selected_remove_ship_index() -> int:
    return st.session_state.selected_remove_ship_index


def is_form_field_disabled(form_field_name: str) -> bool:
    return st.session_state[f"{form_field_name}_disabled"]


def is_remove_ship_confirmed() -> bool:
    return st.session_state.remove_ship_confirmation


def is_session_state_empty() -> bool:
    return len(st.session_state) == 0


def modify_ship_in_current_register(index: int, ship_data: dict) -> None:
    st.session_state.ship_register_current[index] = ship_data


def remove_ship_from_current_register(index: int) -> None:
    if index is not None and index >= 0:
        del st.session_state.ship_register_current[index]


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


def set_remove_ship_confirmation(value: bool) -> None:
    st.session_state.remove_ship_confirmation = value


def set_remove_ship_data(ship_index: int) -> None:
    if ship_index is not None and ship_index >= 0:
        st.session_state.remove_ship_data = get_current_ship_register_list()[
            ship_index
        ]
    if ship_index is None:
        st.session_state.remove_ship_data = []


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

    setup_session_state_for_edit_ship()
    setup_session_state_for_remove_ship()


def setup_session_state_for_edit_ship() -> None:
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


def setup_session_state_for_remove_ship():
    if "remove_selected_ship_index" not in st.session_state:
        st.session_state.remove_selected_ship_index = None

    if "remove_ship_data" not in st.session_state:
        st.session_state.remove_ship_data = []

    if "remove_ship_confirmation" not in st.session_state:
        st.session_state.remove_ship_confirmation = False
