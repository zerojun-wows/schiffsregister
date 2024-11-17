"""
Schiffsregister beginnt mit dieser Datei
"""
import streamlit as st


def main():
    """
    Startpunkt der Schiffsregisteranwendung
    """
    st.title("Schiffsregister")

    st.header("A. Neues oder bestehendes Schiffsregister")

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
