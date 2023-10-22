import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Principal",
        page_icon="",
    )

    st.write("# MEINPS Finance")

    st.sidebar.success("Select a demo above.")

    st.markdown("2023")


if __name__ == "__main__":
    run()
