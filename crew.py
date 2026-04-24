from crewai import Crew, Process
from agents import create_researcher, create_writer, create_judge
from tasks import (
    research_task, 
    write_intro_task, 
    write_seg1_task, 
    write_seg2_task, 
    write_seg3_task, 
    write_outro_task,
    evaluate_task
)

def run_podcast_crew(topic: str):
    """
    Attempts to run the crew and then MANUALLY joins the results 
    to bypass LLM output limits and prevent laziness.
    """
    print(f"--- Hard-Concatenation Mode for: {topic} ---")
    try:
        data = execute_crew(topic, force_ollama=False)
        return data
    except Exception as e:
        print(f"--- Falling back to local engine: {e} ---")
        return execute_crew(topic, force_ollama=True)

def execute_crew(topic: str, force_ollama: bool):
    # Instantiate agents
    researcher = create_researcher(force_ollama)
    writer = create_writer(force_ollama)
    judge = create_judge(force_ollama)

    # Instantiate the 6 segments
    task_res = research_task(researcher, topic)
    task_intro = write_intro_task(writer, topic)
    task_seg1 = write_seg1_task(writer, topic)
    task_seg2 = write_seg2_task(writer, topic)
    task_seg3 = write_seg3_task(writer, topic)
    task_outro = write_outro_task(writer, topic)
    task_eval = evaluate_task(judge, topic)

    # Context chaining
    task_intro.context = [task_res]
    task_seg1.context = [task_res, task_intro]
    task_seg2.context = [task_res, task_seg1]
    task_seg3.context = [task_res, task_seg2]
    task_outro.context = [task_res, task_seg3]
    task_eval.context = [task_intro, task_seg1, task_seg2, task_seg3, task_outro]

    # Form crew
    crew = Crew(
        agents=[researcher, writer, judge],
        tasks=[task_res, task_intro, task_seg1, task_seg2, task_seg3, task_outro, task_eval],
        verbose=True,
        process=Process.sequential,
        memory=False
    )

    crew.kickoff(inputs={'topic': topic})
    
    # MANUAL CONCATENATION: This is the secret to 2000+ words.
    # We join all segment outputs in Python so the LLM never has a chance to summarize them.
    final_combined_script = (
        f"# PODCAST SCRIPT: {topic.upper()}\n\n"
        f"{task_intro.output.raw}\n\n"
        f"## SECTION 1: ORIGINS\n\n{task_seg1.output.raw}\n\n"
        f"## SECTION 2: THE DEEP DIVE\n\n{task_seg2.output.raw}\n\n"
        f"## SECTION 3: IMPACT & LEGACY\n\n{task_seg3.output.raw}\n\n"
        f"## CLOSING\n\n{task_outro.output.raw}"
    )
    
    engine_name = "Local GPU (Ollama)" if force_ollama else "Cloud (Gemini)"
    
    return {
        "engine": engine_name,
        "final_script": final_combined_script,
        "evaluation": task_eval.output.raw,
        "research": task_res.output.raw
    }
