"""
Schiffsregister beginnt mit dieser Datei
"""
import streamlit as st
from data_config import clear_session_state, setup_session_state


def reset_ship_register() -> None:
    """
    Neues Schiffsregister ermöglichen durch Entfernung aller Werte aus dem
    session_state und neu setzen der benötigten Variablen im session_state
    """
    clear_session_state()
    setup_session_state()


def main():
    """
    Startpunkt der Schiffsregisteranwendung
    """
    st.title("Schiffsregister")

    st.header("A. Neues oder bestehendes Schiffsregister")

    if st.button("Neues Schiffsregister"):
        reset_ship_register()

    st.header("B. Aktueller Schiffsbestand")

    st.subheader("B.I Zugänge")

    st.subheader("B.II Änderungen")

    st.subheader("B.III Abgänge")

    st.header("C. Registerbearbeitung")

    st.subheader("C.I Schiff hinzufügen")

    st.subheader("C.II Schiff bearbeiten")

    st.subheader("C.III Schiff entfernen")


if __name__ == "__main__":
    main()
