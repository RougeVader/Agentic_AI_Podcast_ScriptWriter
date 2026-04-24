# System Architecture | AI Podcast Script Writer

## High-Level Flow
The system uses a **Segmented Multi-Agent Architecture** to bypass LLM output limits and ensure high-quality, long-form content (2000+ words).

```mermaid
graph TD
    User((User Input)) -->|Topic| Researcher[Senior Investigative Researcher]
    Researcher -->|Tavily API| Web((The Internet))
    Web -->|Raw Data| Researcher
    Researcher -->|1500+ Word Research Brief| Writer[Lead Podcast Script Architect]

    subgraph "Segmented Writing Phase"
    Writer -->|Task 1| Intro[Intro: 500 words]
    Writer -->|Task 2| Seg1[Origins: 600 words]
    Writer -->|Task 3| Seg2[Deep Dive: 600 words]
    Writer -->|Task 4| Seg3[Impact: 600 words]
    Writer -->|Task 5| Outro[Closing: 400 words]
    end

    subgraph "Verification Phase"
    Intro & Seg1 & Seg2 & Seg3 & Outro --> Judge[Podcast Critic & Judge]
    Judge -->|Score & Critique| EvalTab[Quality Analysis Tab]
    end

    subgraph "Assembly Phase"
    Intro & Seg1 & Seg2 & Seg3 & Outro --> PythonJoin[Python Hard-Concatenation]
    PythonJoin -->|Bypasses LLM Truncation| FinalScript[2000+ Word Masterpiece]
    end

    FinalScript --> Tab1[📜 Production Script Tab]
    EvalTab --> Tab2[📊 Quality Analysis Tab]
    Researcher --> Tab3[🔍 Research Brief Tab]
```

## Key Components
1. **Engine Layer:** Dual-engine support with Grok xAI (Primary) and local Ollama llama3.2 (Hot Fallback).
2. **Research Layer:** Integration with Tavily API for AI-ready search results.
3. **Writing Layer:** Recursive context passing ensures every segment is factually grounded.
4. **UI Layer:** Streamlit-based "Producer's Desk" with typewriter-styled script preview.
