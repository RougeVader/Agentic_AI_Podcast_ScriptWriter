# 🎙️ Agentic AI Podcast ScriptWriter

A professional-grade, multi-agent system designed to research, draft, and critique exhaustive (2000+ word) podcast scripts. Built with **CrewAI**, **Grok xAI**, and **Ollama**.

## 🚀 Submission Checklist
- [x] **GitHub Repository:** Clean code and comprehensive README.
- [x] **Problem Statement:** Detailed in [PROBLEM_STATEMENT.md](./PROBLEM_STATEMENT.md).
- [x] **Task Decomposition:** Documented in [SPEC.md](./SPEC.md) and [tasks.py](./tasks.py).
- [x] **Architecture Diagram:** Visualized in [ARCHITECTURE.md](./ARCHITECTURE.md).
- [x] **Working Agent:** Integrated with Tavily Search, Grok Cloud, and Local LLMs.
- [x] **LLM-as-Judge:** Automated quality scoring and feedback loop.
- [x] **Hot-Fallback:** Seamlessly switches to local GPU if Cloud API fails.

## ⚠️ Deployment & Performance Notes
### STRICT DEPLOYMENT RULE
**DO NOT use Vercel or Railway for this application.**
- **Timeouts:** These platforms have strict 30-60 second execution limits. Because this system is truly **Agentic** (performing deep research and segmented writing), it takes 2-5 minutes to finish. Cloud platforms will kill the process mid-way.
- **RECOMMENDED:** Use **Streamlit Cloud** or **Local Execution**.

### Why Local LLM (Ollama)?
The system is optimized for **Local LLMs (Llama 3.2)** for technical stability:
1. **Bypassing Rate Limits:** Free-tier Cloud APIs often hit "429 Quota Exceeded" during long tasks.
2. **Tool-Calling Stability:** Llama 3.2 3B is specifically tuned for function calling, avoiding the errors common in some Cloud APIs.
3. **Zero Cost:** Generating 2000+ words per session is token-heavy; local execution is free and private.       

## 🧠 The Problem
Most AI writing tools produce short summaries (~500 words) because of LLM output limits. This project solves that by using **Segmented Writing & Hard-Concatenation**, forcing agents to write piece-by-piece to achieve massive, 2000+ word masterpieces with deep technical substance.

## 🛠️ Architecture
The system employs a sophisticated workflow:
1. **Researcher:** Investigates via Tavily API to find 15+ deep facts.
2. **Architect:** Writes five distinct 500+ word segments separately.
3. **Judge:** Scores the script and identifies weaknesses.
4. **Python Assembler:** Manually joins segments to bypass LLM truncation.

> **Full Diagram:** See [ARCHITECTURE.md](./ARCHITECTURE.md) for the Mermaid flowchart.

## 🔌 Setup Instructions
1. **Clone the Repo:**
   ```bash
   git clone https://github.com/RougeVader/Agentic_AI_Podcast_ScriptWriter.git
   cd Agentic_AI_Podcast_ScriptWriter
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment:**
   Create a `.env` file with `XAI_API_KEY` and `TAVILY_API_KEY`.

4. **Run the App:**
   - **Local:** `streamlit run app.py` (Requires Ollama + `llama3.2`)
   - **Streamlit Cloud:** Link this repo and add Secrets to the dashboard.

## 🎥 Flow & Features
- **Dual-Engine:** Uses Grok xAI for speed and Llama 3.2 for local fallback.
- **Museum-Grade UI:** Streamlit "Producer's Desk" with separate tabs for Script, Analysis, and Research.       
- **Strict Word Counts:** Each segment is monitored to ensure the final product hits the 2000-word goal.        
