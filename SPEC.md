# Project Specification | Task Decomposition

## 1. Agent Definitions
| Agent | Role | Focus |
| :--- | :--- | :--- |
| **Researcher** | Investigative Journalist | Finding 15+ deep facts via Tavily Search |
| **Architect** | Lead Scriptwriter | Expanding facts into long-form dialogue (2000+ words) |
| **Judge** | Quality Gate | Evaluating conversational flow, facts, and length |

## 2. Task Breakdown (The Segmented Workflow)
The workload is decomposed into the following sequential steps to ensure high-fidelity output:

1. **Task: Research**
   - Goal: Massive report with at least 15 technical/historical facts.
   - Output: 1000+ words of raw research.

2. **Task: Writing (5-Phase)**
   - **Phase A (Intro):** Cinematic hook and roadmap (500 words).
   - **Phase B (History):** Origins and "The Why" (600 words).
   - **Phase C (Deep Dive):** Technical and niche details (600 words).
   - **Phase D (Impact):** Cultural and human significance (600 words).
   - **Phase E (Closing):** Summary and Outro (400 words).

3. **Task: Critique (LLM-as-Judge)**
   - Goal: Score the script (1-10) and identify "thin" sections.

## 3. Technical Integration
- **Framework:** CrewAI
- **Search Tool:** Tavily API
- **Cloud LLM:** Gemini 2.0 Flash-Lite
- **Local LLM:** Ollama (Llama 3.2 3B)
- **UI:** Streamlit (Multi-Tab layout)
- **Assembly:** Python-based concatenation of task outputs.
