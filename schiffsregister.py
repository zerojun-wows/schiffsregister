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
    # "Bearbeitungsoptionen": []
}

pg = st.navigation(pages)
pg.run()
