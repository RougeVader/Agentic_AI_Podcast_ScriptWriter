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

st.set_page_config(page_title="Producer's Desk | Grok + Ollama", page_icon="🎙️", layout="wide")

# Professional Script Styling
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
    .script-container {
        background-color: #ffffff;
        color: #1a1a1a;
        padding: 50px;
        border-radius: 10px;
        font-family: 'Courier New', Courier, monospace;
        line-height: 1.6;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        max-width: 900px;
        margin: 0 auto;
        font-size: 1.2em;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🎙️ Producer's Desk</h1>", unsafe_allow_html=True)

# Sidebar for Configuration
with st.sidebar:
    st.header("⚙️ System Status")
    xai_key = os.getenv("XAI_API_KEY")
    is_ollama_running, ollama_msg = check_ollama_status()

    if xai_key:
        st.success("🟢 Grok (xAI): Ready")
    else:
        st.warning("🟡 Grok API Key Missing")

    if is_ollama_running:
        st.success("🟢 Local GPU (Ollama): Ready")
    else:
        st.error("🔴 Ollama Offline")

    st.divider()
    st.info("Primary: Grok xAI | Fallback: Local Ollama")

topic = st.text_input("Podcast Topic:", placeholder="e.g., The Secret History of the Roman Empire")

if st.button("Generate Masterpiece 🚀"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        try:
            from crew import run_podcast_crew
            
            with st.spinner("Writing, Critiquing, and Improving your script... This will take a few minutes."):
                data = run_podcast_crew(topic)
            
            st.success(f"✨ Generation Complete! Engine: {data['engine']}")
            
            # THE MULTI-TAB LAYOUT
            tab1, tab2, tab3 = st.tabs(["📜 Production Script", "📊 Quality Analysis", "🔍 Research Brief"])
            
            with tab1:
                st.markdown("<div class='script-container'>", unsafe_allow_html=True)
                st.markdown(data['final_script'])
                st.markdown("</div>", unsafe_allow_html=True)
                
                st.download_button(
                    label="📥 Download Production Script (.md)",
                    data=str(data['final_script']),
                    file_name=f"script_{topic.replace(' ', '_').lower()}.md",
                    mime="text/markdown",
                    use_container_width=True
                )

            with tab2:
                st.header("Critique & Performance Metrics")
                st.markdown(data['evaluation'])
                
            with tab3:
                st.header("Raw Research Intelligence")
                st.markdown(data['research'])

        except Exception as e:
            st.error(f"System Error: {e}")
