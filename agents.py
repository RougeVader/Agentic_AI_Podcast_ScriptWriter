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
    # Handle cases where the LLM might pass a dictionary instead of a string
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

def get_llm():
    # Reverting to stable setup without the unsupported 'config' argument
    return LLM(
        model="ollama/llama3.2", 
        base_url="http://localhost:11434"
    )

def create_researcher():
    return Agent(
        role='Senior Podcast Researcher',
        goal='Conduct deep, exhaustive research on {topic}. Find specific facts, dates, controversy, and behind-the-scenes details. DO NOT make up information if the search fails.',
        backstory='You are a world-class investigative journalist. You never settle for surface-level info. You provide long, detailed research briefs with plenty of substance for the writers.',
        verbose=True,
        allow_delegation=False,
        tools=[tavily_search],
        llm=get_llm(),
        max_iter=5
    )

def create_writer():
    return Agent(
        role='Lead Podcast Writer',
        goal='Draft a compelling, conversational multi-speaker podcast script based directly on the provided research about {topic}.',
        backstory='You are a veteran scriptwriter for hit conversational podcasts. You know how to write dialogue that sounds natural, witty, and flows smoothly between a Host (Alex) and an Expert Guest (Taylor).',
        verbose=True,
        allow_delegation=False,
        llm=get_llm(),
        max_iter=3
    )

def create_editor():
    return Agent(
        role='Executive Producer & Editor',
        goal='Review the draft script about {topic} for pacing, conversational tone, clear speaker labels, and factual accuracy based on the research. Make final edits.',
        backstory='You are the final set of eyes before recording. You ensure the script is not dry, removes robotic language, and checks that Alex and Taylor sound like real humans conversing.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )

def create_judge():
    return Agent(
        role='Podcast Critic & Quality Judge',
        goal='Evaluate the final podcast script for {topic} against high industry standards. Provide a score (1-10) and specific feedback on engagement, flow, and accuracy.',
        backstory='You are a renowned podcast critic. You have high standards for script quality, audience retention, and factual integrity. Your job is to be the final quality gate.',
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )
