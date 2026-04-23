# 🎙️ Multi-Agent Podcast Script Writer

An automated pipeline for researching, writing, and evaluating high-quality conversational podcast scripts using **CrewAI**, **Tavily Search**, and **Google Gemini**.

## 🚀 Features
*   **Multi-Agent Orchestration:** 4 specialized agents working in harmony (Researcher, Writer, Editor, Judge).
*   **Real-time Research:** Integrated with **Tavily Search API** for accurate and up-to-date information.
*   **LLM-as-Judge:** Automated quality scoring and feedback on the final script.
*   **Hybrid LLM Support:** Use **Gemini 1.5 Flash** for speed or **Local Ollama** for privacy.
*   **Conversational Logic:** Specifically tuned to produce natural Host/Guest banter.

## 🛠️ Tech Stack
*   **Agent Framework:** [CrewAI](https://crewai.com)
*   **Search Engine:** [Tavily AI](https://tavily.com)
*   **Language Models:** Google Gemini 1.5 Flash / Ollama (Gemma 3)
*   **Frontend:** Streamlit
*   **Environment:** Python 3.10+

## 📋 Submission Checklist Progress
- [x] GitHub repository with clean code
- [x] Comprehensive README
- [x] Problem statement document (`PROBLEM_STATEMENT.md`)
- [x] Task decomposition / spec document (`SPEC.md`)
- [x] Architecture diagram (`ARCHITECTURE.md`)
- [x] Working agent with API connection (Gemini + Tavily)
- [x] LLM-as-Judge implementation
- [ ] Deployed app - *Ready for Railway/Vercel*

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/Podcast-Script-Writer.git
cd Podcast-Script-Writer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_key
TAVILY_API_KEY=your_tavily_key
```

### 4. Run Locally
```bash
streamlit run app.py
```

## 🧩 Architecture
The system uses a sequential process where research feeds into writing, writing into editing, and editing into final judgment. See [ARCHITECTURE.md](ARCHITECTURE.md) for details.

## 📝 Example Output
The app generates a full markdown script formatted like this:
> **Alex (Host):** Welcome to the show! Today we're diving into...
> **Taylor (Expert):** Thanks Alex. It's fascinating because...

Followed by a **Quality Evaluation Report** giving the script a score and improvement tips.

---
*Built with ❤️ for the Antigravity AI Agent Hackathon.*
