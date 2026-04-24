from crewai import Agent, LLM
from crewai.tools import tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

# Define Tavily Search Tool
@tool("Tavily Search")
def tavily_search(query: str) -> str:
    """Useful to search the web for information. Input should be a single search query string."""
    if isinstance(query, dict):
        query = query.get("query") or query.get("content") or str(query)
    
    try:
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        response = tavily.search(query=query, search_depth="advanced")
        results = response.get('results', [])
        if not results:
            return "No results found for this query."
        return "\n".join([f"Title: {r['title']}\nURL: {r['url']}\nContent: {r['content']}" for r in results])
    except Exception as e:
        return f"Tavily Search failed: {e}"

def get_llm(force_ollama=False):
    xai_key = os.getenv("XAI_API_KEY")
    
    if force_ollama or not xai_key:
        # Local fallback
        return LLM(model="ollama/llama3.2", base_url="http://localhost:11434")

    # Cloud primary
    return LLM(model="xai/grok-beta", api_key=xai_key)

def create_researcher(force_ollama=False):
    return Agent(
        role='Senior Investigative Researcher',
        goal='Conduct a deep investigation into {topic}. You MUST find at least 15 distinct facts. Your output MUST be a long, detailed Markdown report. NEVER just say "Go ahead" or "I am ready."',
        backstory='You are a data-obsessed investigator. You do not talk, you only provide massive amounts of evidence and data points. You hate brevity.',
        verbose=True,
        allow_delegation=False,
        tools=[tavily_search],
        llm=get_llm(force_ollama),
        max_iter=10
    )

def create_writer(force_ollama=False):
    return Agent(
        role='Lead Podcast Script Architect',
        goal='Draft massive conversational script segments for {topic}. You are paid $10 per word. Every point must be expanded into a 5-minute conversation with banter and depth.',
        backstory='You are a verbose scriptwriter. You never summarize. You take a single fact and weave a long, engaging story around it.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm(force_ollama),
        max_iter=10
    )

def create_editor(force_ollama=False):
    return Agent(
        role='Executive Producer & Editor',
        goal='Take the provided script and the critique, and perform a MASSIVE expansion. Your goal is the "Director\'s Cut" – longer, deeper, and more immersive.',
        backstory='You ensure the script is natural and huge. You add the soul to the data.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm(force_ollama),
        max_iter=5
    )

def create_judge(force_ollama=False):
    return Agent(
        role='Podcast Critic & Quality Judge',
        goal='Evaluate the script for {topic} and provide improvement notes. Be harsh about length.',
        backstory='A critic who believes anything under 2000 words is a failure.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm(force_ollama)
    )
