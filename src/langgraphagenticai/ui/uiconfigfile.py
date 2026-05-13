

#Import Python’s built-in tool that reads .ini files.
#Like saying:
#“I need the machine that can read config files.”
from configparser import ConfigParser


#Creating your own blueprint called Config
#Like creating your own helper object.
class Config:
    def __init__(self, config_file="src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config_file = config_file
        self.config.read(self.config_file)

    def get_ollama_models(self): #Create a function to get Ollama models
        return self.config["DEFAULT"].get("OLLAMA_MODELS").split(", ") 
        #Go to this section:[DEFAULT] # Get this value: OLLAMA_MODELS = llama3, mistral, gemma 
        #Split the string into a list: ["Groq", "Ollama"]

    def get_usecase_options(self): #Create a function to get Use Case options
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ") 
        #Go to this section:[DEFAULT] Get this value: USECASE_OPTIONS = Basic Chatbot, Advanced Chatbot
        #Split the string into a list: ["Basic Chatbot", "Advanced Chatbot"]

    def get_page_title(self): #Create a function to get the page title
        return self.config["DEFAULT"].get("PAGE_TITLE") 
        #Go to this section:[DEFAULT] Get this value: PAGE_TITLE = LangGraph : Agentic AI Assistant

    