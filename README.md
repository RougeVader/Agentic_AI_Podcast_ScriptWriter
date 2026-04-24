# 🎙️ Agentic AI Podcast ScriptWriter

A professional-grade, multi-agent system designed to research, draft, and critique exhaustive (2000+ word) podcast scripts.

## ⚠️ STRICT DEPLOYMENT RULE
**DO NOT use Vercel or Railway for this application.** 
- **Vercel/Railway:** These platforms have strict 30-60 second execution timeouts. Because this system is truly **Agentic** (it performs deep research, multi-step reasoning, and segmented writing), it takes 2-5 minutes to produce a masterpiece. Cloud platforms will kill the process before it finishes.
- **RECOMMENDED:** Use **Streamlit Cloud** or **Local Execution**.

## 🧠 Why Local LLM (Ollama)?
While we support Gemini 2.0 Cloud, the system is designed to prioritize **Local LLMs (Llama 3.2)** for several professional reasons:
1. **Bypassing Rate Limits:** Cloud APIs (like Gemini Free Tier) often hit "429 Quota Exceeded" errors during long-form tasks. Local GPUs have no such limits.
2. **Tool-Calling Stability:** We use Llama 3.2 3B, which is specifically optimized for stable function calling, preventing the "beta endpoint" errors common in Cloud APIs.
3. **Zero Cost:** Generating 2000+ words per session is token-intensive. Local execution is completely free and private.

## 🛠️ The "Segmented Writing" Architecture
Most AI tools produce short summaries because they hit a "1000-word output ceiling." This project solves that by:
1. **Piecewise Generation:** 5 distinct agents write separate 500-word segments.
2. **Python Hard-Concatenation:** We join segments using Python code to bypass the LLM's own response limit, ensuring a guaranteed 2000+ word output.

## 🚀 Setup & Submission
1. **Local Run:** `streamlit run app.py` (Requires Ollama + `llama3.2`)
2. **Streamlit Cloud:** Link this GitHub repo to [Streamlit Share](https://share.streamlit.io/).
3. **Secrets:** Add `GEMINI_API_KEY` and `TAVILY_API_KEY` to the Streamlit Secrets dashboard.
