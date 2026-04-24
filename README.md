# 🎙️ Agentic AI Podcast ScriptWriter

A professional-grade, multi-agent system designed to research, draft, and critique exhaustive (2000+ word) podcast scripts. Built with **CrewAI**, **Gemini 2.0**, and **Ollama**.

## 🚀 Submission Checklist
- [x] **GitHub Repository:** Clean code and comprehensive README.
- [x] **Problem Statement:** Detailed in [PROBLEM_STATEMENT.md](./PROBLEM_STATEMENT.md).
- [x] **Task Decomposition:** Documented in [SPEC.md](./SPEC.md) and [tasks.py](./tasks.py).
- [x] **Architecture Diagram:** Visualized in [ARCHITECTURE.md](./ARCHITECTURE.md).
- [x] **Working Agent:** Integrated with Tavily Search, Gemini Cloud, and Local LLMs.
- [x] **LLM-as-Judge:** Automated quality scoring and feedback loop.
- [x] **Hot-Fallback:** Seamlessly switches to local GPU if Cloud API fails.

## 🧠 The Problem
Most AI writing tools produce short, generic summaries (~500 words) because of LLM output limits. This project solves that by using **Segmented Writing & Hard-Concatenation**, forcing the agents to write piece-by-piece to achieve massive, 2000+ word masterpieces with deep technical substance.

## 🛠️ Architecture
The system employs a sophisticated workflow where each agent has a specific, high-iteration role:
1. **Researcher:** Investigates via Tavily API to find 15+ deep facts.
2. **Architect:** Writes five distinct 500+ word segments.
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
   Create a `.env` file with:
   ```env
   GEMINI_API_KEY="your_key_here"
   TAVILY_API_KEY="your_key_here"
   ```

4. **(Optional) Local GPU Fallback:**
   Install [Ollama](https://ollama.com/) and run:
   ```bash
   ollama pull llama3.2
   ```

5. **Run the App:**
   ```bash
   streamlit run app.py
   ```

## 🎥 Flow & Features
- **Dual-Engine:** Uses Gemini 2.0 Flash-Lite for speed and Llama 3.2 for local privacy/fallback.
- **Museum-Grade UI:** Streamlit "Producer's Desk" with separate tabs for Script, Analysis, and Research.
- **Strict Word Counts:** Each segment is monitored to ensure the final product hits the 2000-word goal.
