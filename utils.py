# utils.py

def extract_tech_stack(user_input):
    # Basic comma-separated parsing, can be improved later
    return [tech.strip() for tech in user_input.split(",")]
