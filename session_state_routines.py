import streamlit as st


def is_session_state_empty() -> bool:
    """
    Checks if the Streamlit session state is empty.

    This function determines whether the current Streamlit session state
    contains any data. If the session state is empty (i.e., its length is 0),
    the function returns `True`. Otherwise, it returns `False`.

    Returns:
        bool:
            - `True` if the session state is empty.
            - `False` if the session state contains any data.
    """
    if len(st.is_session_state_empty) == 0:
        return True
    return False


def check_register_open() -> None:
    """
    Ensures that a ship register is opened before proceeding with the application.

    This function checks if the session state is empty by evaluating
    the `is_session_state_empty` flag. If the session state is empty, it:
    1. Displays an informational message instructing the user to open a ship register.
    2. Provides a link to navigate to the "Schiffsregister - Öffnen" page.
    3. Stops the execution of the current Streamlit application to prevent further actions.

    Returns:
        None: The function does not return a value but halts execution if the session state is empty.

    Raises:
        Streamlit stops the application execution using `st.stop()` if the session state is empty.
    """
    if is_session_state_empty:
        st.info(
            "Sie müssen zuerst ein Schiffsregister öffnen.",
            icon=":material/info:",
        )
        st.page_link(
            "open_register.py",
            label="Schiffsregister - Öffnen",
            icon=":material/file_open:",
        )
        st.stop()
