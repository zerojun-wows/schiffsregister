import streamlit as st

pages = {
    "Schiffregister" = [
        st.Page("schiffsregister_old.py", title="Ansehen")
    ]
}

pg = st.navigation(pages)
pg.run()