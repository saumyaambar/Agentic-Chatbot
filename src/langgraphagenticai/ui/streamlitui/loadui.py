import streamlit as st
import os 
from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config() #Create an instance of the Config class to access the configuration settings.
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= " 🐼 " + self.config.get_page_title(), layout="wide")
        st.header("🐼 " + self.config.get_page_title())

        with st.sidebar:
            # LLM Selection
            llm_options = ["Ollama"]
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            
            # Model Selection
            model_options = self.config.get_ollama_models()
            self.user_controls["selected_ollama_model"] = st.selectbox("Select Model", model_options)

            # Use Case Selection
            usecase_options = self.config.get_usecase_options()
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase", usecase_options)

        return self.user_controls  
