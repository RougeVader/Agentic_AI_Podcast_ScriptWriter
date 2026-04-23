# System Architecture: Multi-Agent Podcast Script Writer

## High-Level Architecture
The application follows a modular, agent-based architecture coordinated by the CrewAI framework.

```mermaid
graph TD
    User((User)) --> Streamlit[Streamlit Frontend]
    Streamlit --> Crew[CrewAI Orchestrator]
    
    subgraph AI Team
        Researcher[Senior Researcher]
        Writer[Lead Writer]
        Editor[Executive Editor]
        Judge[Podcast Critic]
    end
    
    Crew --> Researcher
    Researcher --> Tavily[Tavily Search API]
    Tavily --> Researcher
    
    Researcher --> Writer
    Writer --> Editor
    Editor --> Judge
    
    Judge --> Crew
    Crew --> Streamlit
    Streamlit --> User
    
    subgraph LLM Providers
        Gemini[Google Gemini 1.5 Flash]
        Ollama[Local Ollama / Gemma 3]
    end
    
    Researcher -.-> Gemini
    Writer -.-> Gemini
    Editor -.-> Gemini
    Judge -.-> Gemini
```

## Component Breakdown

### 1. Frontend (Streamlit)
*   Handles user input (Topic, API Keys).
*   Displays real-time status updates and final outputs.
*   Provides download links for the generated script.

### 2. Orchestration (CrewAI)
*   Manages the state and memory between agents.
*   Executes tasks in a sequential process (Process.sequential).
*   Handles LLM interactions via the `LLM` class.

### 3. Agents & Tools
*   **Researcher:** Equipped with the `Tavily Search` tool for deep web searching.
*   **Writer:** Context-aware agent that consumes research data.
*   **Editor:** Quality control agent focused on tone and formatting.
*   **Judge:** Implementation of the **LLM-as-Judge** pattern to provide an objective score.

### 4. External Integrations
*   **Tavily API:** Used for high-quality, AI-optimized search results.
*   **Gemini API:** Primary cloud LLM for deployment.
*   **Ollama (Fallback):** Supports local development and privacy-focused execution.
