import streamlit as st

st.title("Schiffsregister - Ausgeben")

if len(st.session_state) == 0:
    st.info(
        "Damit etwas angezeigt werden kann muss zunächst ein Schiffsregister geöffnet werden."
    )
