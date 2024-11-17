"""
Schiffsregister beginnt mit dieser Datei
"""
import streamlit as st


def main():
    st.title("Schiffsregister")

    st.header("A. Neues oder bestehendes Schiffsregister")

    st.header("B. Aktueller Schiffsbestand")

    st.subheader("Zugänge")

    st.subheader("Änderungen")

    st.subheader("Abgänge")

    st.header("C. Registerbearbeitung")

    st.subheader("Schiff hinzufügen")

    st.subheader("Schiff bearbeiten")

    st.subheader("Schiff entfernen")


if __name__ == "__main__":
    main()
