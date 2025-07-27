# chatbot.py

from prompts import generate_questions_prompt
from utils import extract_tech_stack
import openai
import os
from dotenv import load_dotenv
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class HiringAssistant:
    def __init__(self):
        self.user_data = {}
        self.stage = "greeting"
        self.questions = []
        self.current_question_idx = 0

    def respond(self, user_input):
        user_input = user_input.strip()

        if self.stage == "greeting":
            self.stage = "collect_name"
            return "Hi! May I know your full name?"

        elif self.stage == "collect_name":
            self.user_data["name"] = user_input
            self.stage = "collect_email"
            return "Thanks! What's your email address?"

        elif self.stage == "collect_email":
            self.user_data["email"] = user_input
            self.stage = "collect_phone"
            return "Got it. What's your phone number?"

        elif self.stage == "collect_phone":
            self.user_data["phone"] = user_input
            self.stage = "collect_experience"
            return "How many years of experience do you have?"

        elif self.stage == "collect_experience":
            self.user_data["experience"] = user_input
            self.stage = "collect_position"
            return "What position are you applying for?"

        elif self.stage == "collect_position":
            self.user_data["position"] = user_input
            self.stage = "collect_location"
            return "Where are you currently located?"

        elif self.stage == "collect_location":
            self.user_data["location"] = user_input
            self.stage = "collect_tech_stack"
            return "Please list your tech stack (e.g., Python, Django, MySQL):"

        elif self.stage == "collect_tech_stack":
            self.user_data["tech_stack"] = extract_tech_stack(user_input)
            self.questions = self.generate_questions_list()
            self.stage = "ask_questions"
            return self.questions[self.current_question_idx]

        elif self.stage == "ask_questions":
            self.current_question_idx += 1
            if self.current_question_idx < len(self.questions):
                return self.questions[self.current_question_idx]
            else:
                self.stage = "generate_questions"
                return "Thank you for your answers. Would you like to continue or exit?"

        elif self.stage == "generate_questions":
            if user_input.lower() in ["exit", "quit", "bye"]:
                self.stage = "end"
                return f"Thanks {self.user_data.get('name', '')}! We'll get back to you soon."
            elif user_input.lower() in ["yes", "y", "continue"]:
                self.stage = "follow_up"
                return "Great! You can tell me more or ask anything else."
            else:
                return "Would you like to continue or exit?"

        elif self.stage == "follow_up":
            return "You're still connected. Let me know how I can help further."

        elif self.stage == "end":
            return "This session is closed. Thank you!"

        else:
            return "I'm not sure how to respond. Could you please rephrase?"

    def generate_questions_list(self):
        tech_stack = self.user_data.get("tech_stack", [])
        position = self.user_data.get("position", "the role")

        if {"python", "sql"}.issubset(set(tech_stack)):
            return [
                f"1. Explain how you'd optimize a SQL query for better performance in {position}.",
                f"2. What are Python generators and how can they help in data processing?",
                f"3. How would you handle large datasets in Python for analytics or ETL tasks?",
                f"4. Describe a real-world scenario where you used JOINs in SQL effectively.",
                f"5. How would you implement error handling in a Python script used for automation?"
            ]
        elif any(tech in tech_stack for tech in ["java", "javascript", "react"]):
            return [
                f"1. Describe how you would manage state in a complex React application for {position}.",
                f"2. How does asynchronous programming work in JavaScript? Give examples.",
                f"3. What are the main principles of OOP in Java? How do they help with application design?",
                f"4. Explain the lifecycle of a React component and how you can use hooks effectively.",
                f"5. How would you handle API integration and error handling in a front-end React app?"
            ]
        else:
            try:
                prompt = generate_questions_prompt(tech_stack)
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                return response['choices'][0]['message']['content'].split('\n')
            except Exception:
                return ["Sorry, I couldn't generate questions using the API."]
