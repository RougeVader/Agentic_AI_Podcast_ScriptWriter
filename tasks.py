from crewai import Task

def research_task(agent, topic):
    return Task(
        description=f"Conduct thorough research on the topic: '{topic}'. Find recent news, key facts, and interesting stories. Compile a comprehensive research brief. Provide URLs if applicable.",
        expected_output="A structured research brief containing bullet points of key facts, recent news, and 2-3 unique angles for the podcast.",
        agent=agent
    )

def write_script_task(agent, topic):
    return Task(
        description=f"Using the deep research provided, write a LONG and ENGAGING podcast script about '{topic}'. "
                    f"The script must be at least 1500 words and feel like a full 15-minute episode. "
                    f"Structure: 1) High-energy Intro with a compelling hook. 2) 4-5 Detailed Segments exploring different facets of the topic. 3) Deep-dive analysis and expert insights from Taylor. 4) Outro with detailed takeaways. "
                    f"Use format 'Alex (Host):' and 'Taylor (Expert):'. "
                    f"Your output MUST be plain Markdown text. Do NOT start your response with '{{' or any JSON structure.",
        expected_output="A comprehensive, multi-page podcast script with professional formatting, stage directions [in brackets], and rich dialogue.",
        agent=agent
    )

def edit_script_task(agent, topic):
    return Task(
        description=f"Review the 1500+ word podcast script about '{topic}'. "
                    f"1. Expand on any sections that feel rushed. "
                    f"2. Ensure the dialogue sounds 100% natural and conversational. "
                    f"3. Use professional markdown formatting (Bold speaker names, clear headers, italicized stage directions). "
                    f"CRITICAL: Your final answer MUST be ONLY the script content in Markdown. Never return JSON or tool-call syntax.",
        expected_output="The final, definitive, and long-form podcast script in markdown. No summaries, no notes, just the script.",
        agent=agent
    )

def evaluate_script_task(agent, topic):
    return Task(
        description=f"Judge the quality of the final podcast script for '{topic}'. "
                    f"Score it from 1 to 10 based on conversational quality, research depth, and entertainment value. "
                    f"Provide a brief justification for your score and suggest any minor improvements if needed. "
                    f"Your final answer MUST be a structured markdown report, NOT a tool call.",
        expected_output="A quality evaluation report including a numeric score and critical feedback in markdown format.",
        agent=agent
    )
