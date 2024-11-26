import streamlit as st

pages = {
    "Schiffsregister": [
        st.Page("show_register.py", title="Ansehen", icon=":material/news:"),
        st.Page(
            "open_register.py", title="Öffnen", icon=":material/file_open:"
        ),
        st.Page(
            "dump_register.py", title="Ausgeben", icon=":material/file_save:"
        ),
    ],
    "Bearbeitungsoptionen": [
        st.Page(
            "add_ship.py", title="Schiff hinzufügen", icon=":material/add:"
        ),
        st.Page(
            "modify_ship.py", title="Schiff bearbeiten", icon=":material/edit:"
        ),
        st.Page(
            "remove_ship.py", title="Schiff entfernen", icon=":material/remove:"
        ),
    ],
}

pg = st.navigation(pages)
pg.run()
