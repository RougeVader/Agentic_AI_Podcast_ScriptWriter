# Problem Statement | AI Podcast Script Writer

## The Challenge: "The 500-Word Ceiling"
Most current AI writing agents suffer from **"Contextual Laziness"** and **"Output Truncation"**. When asked to write a long-form podcast script (e.g., 2000+ words), they typically:
1. Provide a short summary instead of a full script.
2. Hit the hard output token limit of the LLM (~1000 words) and stop mid-sentence.
3. Lose factual depth as they prioritize finishing the response over detail.

## The Objective
To build an agentic system that can:
- **Research:** Autonomously gather high-quality, technical facts using Tavily.
- **Scale:** Guarantee a word count of 2000+ words without truncation.
- **Qualify:** Automatically critique its own work (LLM-as-Judge) to ensure it sounds like a professional human conversation.
- **Persist:** Maintain operation even if Cloud APIs fail or hit rate limits.

## The Solution
We solve this using a **Segmented Multi-Agent Architecture**:
- **Role Specialization:** Each agent (Researcher, Architect, Judge) is tuned for extreme verbosity and high iteration.
- **Piecewise Generation:** The script is written in 5 distinct segments (Intro, History, Tech, Human, Future), each targeting 400-600 words.
- **Python Hard-Concatenation:** We bypass the LLM's own response limit by joining these segments in Python, ensuring zero loss of content.
- **Hot-Fallback Logic:** A "dual-engine" approach that automatically switches from Gemini Cloud to a local NVIDIA GPU (via Ollama) upon any failure.
