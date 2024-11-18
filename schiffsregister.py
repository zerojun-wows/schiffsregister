"""
Schiffsregister beginnt mit dieser Datei
"""
import hashlib
import pandas as pd
import streamlit as st

from data_config import clear_session_state, setup_session_state


def reset_ship_register() -> None:
    """
    Neues Schiffsregister ermöglichen durch Entfernung aller Werte aus dem
    session_state und neu setzen der benötigten Variablen im session_state.
    """
    clear_session_state()
    setup_session_state()


def upload_file() -> None:
    """
    Formular zum Hochladen einer Datei sowie Prüfung der Dateistruktur auf die
    Hauptspalten.
    """
    uploaded_file = st.file_uploader(
        "Wählen Sie eine Schiffsregister-Datei zum Hochladen", type="csv"
    )
    if uploaded_file is not None:
        file_hash = hashlib.sha256(uploaded_file.read()).hexdigest()

        if file_hash != st.session_state.last_uploaded_file_hash:
            uploaded_file.seek(0)

            df = pd.read_csv(uploaded_file)

            missing_columns = [
                col for col in main_columns if col not in df.columns
            ]
            extra_columns = [
                col for col in df.columns if col not in main_columns
            ]
            if missing_columns:
                st.error(f"Fehlende Spalten: {', '.join(missing_columns)}")
            if extra_columns:
                st.warning(f"Zusätzliche Spalten: {', '.join(extra_columns)}")

            if not missing_columns and not extra_columns:
                st.session_state.schiffsregister_aktuell = df.to_dict(
                    orient="records"
                )
                st.session_state.schiffsregister_original = df.to_dict(
                    orient="records"
                )
                st.session_state.last_uploaded_file_hash = file_hash
                st.success("Schiffsregister erfolgreich geladen!")
            else:
                st.warning(
                    "Die Datei wurde aufgrund von Spaltenproblemen nicht hochgeladen."
                )
        else:
            st.info("Dieses Schiffsregister ist bereits geladen.")


def main():
    """
    Startpunkt der Schiffsregisteranwendung
    """
    setup_session_state()

    st.title("Schiffsregister")

    st.header(
        "A. Neues oder bestehendes Schiffsregister",
        "neues-oder-bestehendes-schiffsregister",
    )

    if st.button("Neues Schiffsregister"):
        reset_ship_register()

    upload_file()

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
