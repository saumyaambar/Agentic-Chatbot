import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI


def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI. 
    This function initializes the UI, handles user input, configures the LLM model, 
    sets up the graph based on the selected use case, and displays the output
    while implementing exception handling for robustness. 
    """
    #Load UI:
    ui = LoadStreamlitUI() #Create an instance of the LoadStreamlitUI class to manage the UI.
    user_input = ui.load_streamlit_ui() #Load the Streamlit UI and get the user's selections.

    if not user_input: #If no user input is received, display a warning message and exit the function.
        st.error("Error: Failed to load user input from the UI.")
        return
    
    user_message = st.chat_input("Enter your message:") #Create a chat input box for the user to enter their message.


    