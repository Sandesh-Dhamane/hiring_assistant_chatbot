# prompts.py

def generate_questions_prompt(tech_stack):
    techs = ", ".join(tech_stack)
    return (
        f"You are a technical interviewer. Generate 3 to 5 challenging technical interview questions "
        f"based on the following tech stack: {techs}.\n"
        f"Each question should test the candidate's real understanding."
    )
