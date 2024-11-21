import streamlit as st

pages = {"Schiffsregister": [st.Page("show_register.py", title="Ansehen")]}

pg = st.navigation(pages)
pg.run()
