import streamlit as st

pages = {
    "Schiffsregister": [
        st.Page("show_register.py", title="Ansehen"),
        st.Page("open_register.py", title="Öffnen"),
        st.Page("dump_register.py", title="Ausgeben"),
    ],
    # "Bearbeitungsoptionen": []
}

pg = st.navigation(pages)
pg.run()
