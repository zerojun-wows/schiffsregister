import streamlit as st

st.title("Schiffsregister - Öffnen")

st.write(
    f"Sie können ein neues leeres Schiffsregister eröffnen, oder "
    f"ein bestehendes Schiffsregister hochladen."
)

if st.button("Neues Schiffsregister eröffnen"):
    # clear session_state
    # set session_state variables
    pass

st.write(st.session_state)
