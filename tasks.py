from crewai import Task

def research_task(agent, topic):
    return Task(
        description=f"Find 15+ deep facts about '{topic}'. Focus on technical details and untold stories. "
                    f"Output a long Markdown report.",
        expected_output="A massive research report.",
        agent=agent
    )

def write_intro_task(agent, topic):
    return Task(
        description=f"Write a 500-word INTRO for '{topic}'. Include a cinematic hook and host banter. "
                    f"Format: 'Alex (Host):' and 'Taylor (Expert):'.",
        expected_output="500+ words of Intro dialogue.",
        agent=agent
    )

def write_seg1_task(agent, topic):
    return Task(
        description=f"Write a 600-word SEGMENT 1 (Origins) for '{topic}'. Go into extreme detail. "
                    f"Format: 'Alex (Host):' and 'Taylor (Expert):'.",
        expected_output="600+ words of Origins dialogue.",
        agent=agent
    )

def write_seg2_task(agent, topic):
    return Task(
        description=f"Write a 600-word SEGMENT 2 (Technical Deep Dive) for '{topic}'. Explore the 'how' in depth. "
                    f"Format: 'Alex (Host):' and 'Taylor (Expert):'.",
        expected_output="600+ words of Technical dialogue.",
        agent=agent
    )

def write_seg3_task(agent, topic):
    return Task(
        description=f"Write a 600-word SEGMENT 3 (Impact & Cultural Significance) for '{topic}'. "
                    f"Format: 'Alex (Host):' and 'Taylor (Expert):'.",
        expected_output="600+ words of Impact dialogue.",
        agent=agent
    )

def write_outro_task(agent, topic):
    return Task(
        description=f"Write a 400-word OUTRO for '{topic}'. Summarize the journey and give a final verdict. "
                    f"Format: 'Alex (Host):' and 'Taylor (Expert):'.",
        expected_output="400+ words of Outro dialogue.",
        agent=agent
    )

def evaluate_task(agent, topic):
    return Task(
        description=f"Critique the FULL research and script segments for '{topic}'. "
                    f"Point out any inconsistencies between the facts found and the dialogue written.",
        expected_output="A list of quality improvements.",
        agent=agent
    )
