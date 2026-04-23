# Technical Specification: Multi-Agent Podcast Script Writer

## 1. Overview
A multi-agent system built using CrewAI that automates the end-to-end process of researching and writing podcast scripts. The system features a Streamlit frontend, integrates with Tavily Search for real-time data, and utilizes an LLM-as-Judge pattern for quality assurance.

## 2. Agent Roles (Task Decomposition)
The system decomposes the complex task of script writing into four specialized agents:

### A. Senior Podcast Researcher
*   **Goal:** Gather facts, news, and unique angles on the topic.
*   **Tool:** Tavily Search.
*   **Output:** Structured research brief.

### B. Lead Podcast Writer
*   **Goal:** Convert research into a conversational script between Alex (Host) and Taylor (Expert).
*   **Constraint:** Must sound natural, not like an essay.

### C. Executive Producer & Editor
*   **Goal:** Refine dialogue, fix pacing, and ensure consistent speaker tags.
*   **Output:** Polished markdown script.

### D. Podcast Critic (LLM-as-Judge)
*   **Goal:** Evaluate the final script against professional standards.
*   **Output:** 1-10 score and critical feedback.

## 3. Technology Stack
*   **Framework:** CrewAI (Agent Orchestration)
*   **LLMs:** Google Gemini 1.5 Flash (via API) or Ollama/Gemma3:4b (Local Fallback)
*   **Search Engine:** Tavily API
*   **Frontend:** Streamlit
*   **Deployment:** Railway or Vercel

## 4. Workflow
1.  **Input:** User provides a topic in the Streamlit UI.
2.  **Research:** The Researcher agent queries Tavily Search for the latest info.
3.  **Drafting:** The Writer agent receives the research and generates the first draft.
4.  **Editing:** The Editor agent polishes the draft.
5.  **Judging:** The Critic agent evaluates the polished script.
6.  **Output:** The final script and the evaluation report are displayed to the user.

## 5. Verification Plan
*   **Research Quality:** Check URLs and factual accuracy in the research brief.
*   **Conversational Flow:** Manually verify that the script uses Host/Guest banter.
*   **Judge Reliability:** Ensure the critic provides constructive feedback, not just a score.
