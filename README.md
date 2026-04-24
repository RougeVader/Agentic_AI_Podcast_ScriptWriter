# 🎙️ Agentic Podcast Script Writer (Grok + Ollama)

A professional-grade, multi-agent system that writes massive (2000+ words) podcast scripts using **Grok xAI** and local **Ollama**.

## 🚀 Key Features
- **Grok xAI Integration:** High-quality script generation as the primary engine.
- **Local GPU Fallback:** Automatically switches to **Ollama (llama3.2)** if the cloud API is unavailable.
- **Segmented Writing:** Bypasses LLM output limits by writing scripts piece-by-piece and concatenating them.
- **Tavily Research:** Deep-web searching for real-time, accurate facts.
- **LLM-as-Judge:** Renowned critic agent scores every script before delivery.

## 🛠️ Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment:**
   Create a `.env` file:
   ```env
   XAI_API_KEY="your-grok-key"
   TAVILY_API_KEY="your-tavily-key"
   ```

3. **Local AI (Optional):**
   Install [Ollama](https://ollama.com) and pull the model:
   ```bash
   ollama pull llama3.2
   ```

4. **Run Application:**
   ```bash
   streamlit run app.py
   ```

## 🧠 The AI Crew
- **Senior Researcher:** Investigates the topic using Tavily Search.
- **Lead Script Architect:** Drafts the dialogue with a focus on length and banter.
- **Quality Judge:** Provides a harsh critique and numerical score.

## 📝 Output Format
The system produces a professionally formatted Markdown script with:
- **Bold Speaker Names** (Alex & Taylor)
- *Italicized Stage Directions*
- Clear segment headers for production.
