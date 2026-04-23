from crewai import Crew, Process
from agents import create_researcher, create_writer, create_editor, create_judge
from tasks import research_task, write_script_task, edit_script_task, evaluate_script_task

def run_podcast_crew(topic: str):
    # Instantiate agents
    researcher = create_researcher()
    writer = create_writer()
    editor = create_editor()
    judge = create_judge()

    # Instantiate tasks
    task1 = research_task(researcher, topic)
    task2 = write_script_task(writer, topic)
    task3 = edit_script_task(editor, topic)
    task4 = evaluate_script_task(judge, topic)

    # Form the crew
    crew = Crew(
        agents=[researcher, writer, editor, judge],
        tasks=[task1, task2, task3, task4],
        verbose=True,
        process=Process.sequential,
        memory=False
    )

    # Kickoff the process
    result = crew.kickoff(inputs={'topic': topic})
    
    # The result object contains the final task's output by default
    # But we might want the script (task3) and the evaluation (task4)
    # However, kickoff returns the final output.
    # To get both, we can access task outputs.
    
    final_output = f"## Final Podcast Script\n\n{task3.output.raw}\n\n---\n## Quality Evaluation (LLM-as-Judge)\n\n{task4.output.raw}"
    
    return final_output
