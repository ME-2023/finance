import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Principal",
        page_icon="",
    )

    st.write("# MEINPS Finance")
    st.write("# Data Science Web App")
    st.write("""
    MEINPS Finance is a project that focuses its efforts on the study of collective economic behavior 
    through AI and Data Science. It aims to integrate knowledge from different domains of the 
    human being, applied to collective human behavior.
    
    MEINPS considers that the most evolved aspects of the human being are defined by collective 
    processes and that these have a digital extension. The human being at the beginning of the 
    21st century has a Digital Collective Behavior.
    
    The ontological foundation of MEINPS's actions is found in cooperative and empathetic work 
    between people; the epistemological basis is found in the scientific method.
    """)

    st.sidebar.success("Select a demo above.")

    st.markdown("2023")


if __name__ == "__main__":
    run()
