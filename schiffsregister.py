import streamlit as st

pages = {
    "Schiffsregister": [st.Page("schiffsregister_old.py", title="Ansehen")]
}

pg = st.navigation(pages)
pg.run()
