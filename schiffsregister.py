"""
Schiffsregister beginnt mit dieser Datei
"""
import streamlit as st


def main():
    st.title("Schiffsregister")

    st.header("Neues oder bestehendes Schiffsregister")

    st.header("Aktueller Schiffsbestand")

    st.subheader("Zugänge")

    st.subheader("Änderungen")

    st.subheader("Abgänge")

    st.header("Registerbearbeitung")

    st.subheader("Schiff hinzufügen")

    st.subheader("Schiff bearbeiten")

    st.subheader("Schiff entfernen")


if __name__ == "__main__":
    main()
