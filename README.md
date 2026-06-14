# LangGraph Agentic AI Chatbot

An AI-powered chatbot built using LangGraph, LangChain, Streamlit, and Groq LLMs with a state-driven conversational workflow.

---

## Features
- Interactive chat interface built with Streamlit
- State-driven conversational workflow using LangGraph StateGraph
- Multiple LLM model support via Groq API (Llama 3.3 70B, Gemma2 9B)
- Dynamic model selection from the UI sidebar
- Modular and scalable architecture

---

## Tech Stack
- Python
- LangGraph
- LangChain
- Streamlit
- Groq API (Llama 3.3 70b-versatile, Gemma2-9b-it)

---
## Project Structure
├── app.py                        # Entry point

├── requirements.txt              # Dependencies

└── src/

└── langgraphagenticai/

├── graph/

│   └── graph_builder.py  # LangGraph StateGraph setup

├── LLMs/

│   └── groqllm.py        # Groq LLM configuration

├── nodes/

│   └── basic_chatbot_node.py  # Chatbot node logic

├── state/

│   └── state.py          # State structure definition

├── ui/

│   └── streamlitui/

│       ├── loadui.py         # Streamlit UI loader

│       ├── display_result.py # Result display handler

│       └── uiconfigfile.ini  # UI configuration

└── main.py               # App orchestration


---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/saumyaambar/your-repo-name
cd your-repo-name
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

4. In the sidebar:
   - Select **Groq** as LLM
   - Enter your **Groq API Key** (get it from [console.groq.com](https://console.groq.com/keys))
   - Select a model (Llama 3.3 70B or Gemma2 9B)
   - Select use case: **Basic Chatbot**

---

## Architecture
- `StateGraph` manages the conversational state using LangGraph
- Each message is processed through the `BasicChatbotNode`
- Groq API handles LLM inference
- Streamlit renders the chat interface dynamically

---

## Objective
To build a modular, scalable AI chatbot leveraging LangGraph's state-driven architecture with support for multiple LLMs through Groq's fast inference API.
