import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Ensure we load env before anything else
load_dotenv()

def check_ollama_status():
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            return True, "Ollama is running."
        return False, f"Ollama returned unexpected status: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "Ollama connection refused."
    except Exception as e:
        return False, f"Ollama check failed: {e}"

st.set_page_config(page_title="Multi-Agent Podcast Writer", page_icon="🎙️", layout="wide")

# Custom UI styling
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    .main-title {
        background: -webkit-linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: 800;
        margin-bottom: 20px;
    }
    .info-box {
        background: rgba(255, 255, 255, 0.05);
        border-left: 4px solid #4ECDC4;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 1.1em;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(78, 205, 196, 0.4);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🎙️ Multi-Agent Podcast Script Writer</h1>", unsafe_allow_html=True)
st.markdown("<div class='info-box'>Powered by <strong>CrewAI</strong>, <strong>Tavily Search</strong>, and <strong>LLM-as-Judge</strong>. AI agents collaborate to create high-quality podcast scripts.</div>", unsafe_allow_html=True)

# Sidebar for Configuration
with st.sidebar:
    st.header("⚙️ Configuration")

    is_running, msg = check_ollama_status()
    if is_running:
        st.success("🟢 AI Engine: Ollama Online")
        st.info("Using local RTX 3050 GPU with llama3.2 for processing.")
    else:
        st.error(f"🔴 AI Engine: Offline")
        st.warning(f"Ollama check failed: {msg}")
        st.info("Please ensure 'ollama serve' is running and you have run 'ollama pull llama3.2'.")


topic = st.text_input("Enter a Topic for the Podcast:", placeholder="e.g., The Future of Quantum Computing in Healthcare")

if st.button("Generate Script 🚀"):
    if not (os.getenv("GEMINI_API_KEY") or check_ollama_status()[0]):
        st.error("No LLM engine available. Please provide an API key or start Ollama.")
    elif not os.getenv("TAVILY_API_KEY"):
        st.error("Tavily API Key is required for research.")
    elif not topic:
        st.warning("Please enter a topic.")
    else:
        st.info(f"Assembling AI Crew to research and write about: **{topic}**...")
        
        try:
            from crew import run_podcast_crew
            
            with st.spinner("The AI Crew is working... Researching via Tavily, drafting a long-form script, and performing final evaluation."):
                final_output = run_podcast_crew(topic)
            
            st.success("✨ Generation Complete!")
            
            # Displaying the output in a clean, full-width container
            output_container = st.container()
            with output_container:
                st.markdown(final_output)
            
            st.divider()
            st.download_button(
                label="📥 Download Full Markdown Script",
                data=str(final_output),
                file_name=f"podcast_{topic.replace(' ', '_').lower()}.md",
                mime="text/markdown",
                use_container_width=True
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")
