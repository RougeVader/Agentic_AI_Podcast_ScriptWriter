# Architecture: Agentic Podcast Script Writer

This system uses a **multi-agent orchestration pattern** powered by **CrewAI** and **Grok xAI** (with local **Ollama** fallback) to research and write long-form, professional podcast scripts.

## 1. The Engine
- **Primary Engine:** Grok xAI (`grok-beta`) for high-speed, long-context reasoning.
- **Local Fallback:** Ollama (`llama3.2`) running on local NVIDIA RTX 3050 GPU.
- **Search Engine:** Tavily API for high-quality, AI-ready research data.

## 2. Multi-Agent Pipeline
The process is broken into sequential stages to ensure depth and prevent LLM truncation:

### Stage 1: Deep Research
- **Agent:** Senior Investigative Researcher
- **Task:** Exhaustive search via Tavily. Compiles a massive research brief with 15+ facts.

### Stage 2: Segmented Writing (The Secret to Length)
Instead of writing the whole script at once, the system writes in chapters:
1. **Intro:** High-energy hook and setup.
2. **Origins:** Historical context/background.
3. **The Deep Dive:** Technical/Scientific/Detailed analysis.
4. **Impact:** Current relevance and controversy.
5. **Closing:** Key takeaways and outro.

### Stage 3: Quality Control
- **Agent:** Podcast Critic & Quality Judge
- **Task:** Scores the combined script (1-10) and provides a detailed critique.

## 3. Data Flow
1. User enters **Topic**.
2. **Researcher** hits Tavily API -> Returns JSON/Markdown research.
3. **Writer** iterates through 5 separate segments, each building on the previous one's context.
4. **System** manually concatenates the results in Python to ensure a **2000+ word** final output.
5. **Critic** performs "LLM-as-Judge" evaluation.

## 4. UI Layer
- **Streamlit:** Provides a dark-themed, professional dashboard.
- **Multi-Tab Output:** Separate views for the Script, the Evaluation, and the Raw Research.
