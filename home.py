import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Principal",
        page_icon="",
    )

    st.write("# MEINPS Finanzas")
    st.write("# Data Science Web App")
    st.write("""
    MEINPS Finanzas es un proyecto que centra sus 
    esfuerzos en el estudio del comportamiento 
    económico colectivo a través de la IA y la 
    Ciencia de Datos. Pretende integrar conocimientos 
    procedentes de diferentes ámbitos del ser humano, 
    aplicados al comportamiento humano colectivo.
    
    MEINPS considera que los aspectos más evolucionados 
    del ser humano están definidos por procesos 
    colectivos y que estos tienen una extensión digital. 
    El ser humano a inicios del siglo XXI tiene un 
    Comportamiento Colectivo Digital.
             
    El fundamento ontológico del accionar del MEINPS se 
    encuentra en el trabajo cooperativo y empático 
    entre personas; la base epistemológica se encuentra 
    en el método científico.
    """)

    st.sidebar.success("Seleccionar una opción.")

    st.markdown("2023")


if __name__ == "__main__":
    run()
