import streamlit as st

from session_state_routines import (
    check_register_open,
    get_current_ship_register_dataframe,
    get_additions_dataframe,
    get_modifications_dataframe,
    get_removals_dataframe,
)

df_column_config = {
    "Nation": st.column_config.TextColumn(width=None),
    "Typ": st.column_config.TextColumn(width=None),
}

st.title("Schiffsregister - Ansicht")

check_register_open()

st.subheader("Aktueller Bestand")

current_ship_register_df = get_current_ship_register_dataframe()

if current_ship_register_df.empty:
    st.info("Noch keine Einträge vorhanden", icon=":material/info:")
else:
    st.dataframe(current_ship_register_df, column_config=df_column_config)

# additions
st.subheader("Zugänge")

if current_ship_register_df.empty or get_additions_dataframe().empty:
    st.info("Keine Zugänge vorhanden", icon=":material/info:")
else:
    st.dataframe(get_additions_dataframe())

# modifications
st.subheader("Änderungen")

if current_ship_register_df.empty or get_modifications_dataframe().empty:
    st.info("Keine Änderungen vorhanden", icon=":material/info:")
else:
    st.dataframe(get_modifications_dataframe())

# removals
st.subheader("Abgänge")

if current_ship_register_df.empty or get_removals_dataframe().empty:
    st.info("Keine Abgänge vorhanden", icon=":material/info:")
else:
    st.dataframe(get_removals_dataframe())
