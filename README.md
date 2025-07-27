# 💼 Hiring Assistant Chatbot

## 🧠 Project Overview

The **Hiring Assistant Chatbot** is a conversational web application built using **Streamlit** and **LLMs (via Hugging Face or OpenAI APIs)**. It simulates a recruiter conducting a screening interview. The assistant collects candidate information (like name, experience, tech stack, etc.) and dynamically generates technical questions based on the candidate's inputs. The conversation mimics a real interview-style flow with one question at a time and context-aware responses.

---

## 🛠 Installation Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/hiring-assistant-chatbot.git
cd hiring-assistant-chatbot
2. Create and Activate Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
3. Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root directory and add your Hugging Face or OpenAI API key:

env
Copy
Edit
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
OPENAI_API_KEY=your_openai_api_key
🚀 Usage Guide
To run the chatbot locally, use the following command:

bash
Copy
Edit
streamlit run app.py
Once running, the chatbot UI will open in your default browser. The assistant will:

Greet the user

Ask for candidate details (name, email, tech stack, etc.)

Dynamically generate interview questions based on the tech stack

Ask questions one at a time in a conversational format

Provide an option to continue or exit

⚙️ Technical Details
Frontend/UI: Streamlit

LLM APIs: OpenAI GPT-3.5/4, HuggingFace Transformers

Language: Python 3.x

Key Libraries:

openai – for OpenAI-based generation

requests – for Hugging Face API

dotenv – for managing environment variables

streamlit – for UI interaction

Architecture:

chatbot.py handles conversation flow and LLM logic

app.py handles user interface

prompts.py manages reusable prompt templates

utils.py contains helper functions

✍️ Prompt Design
Prompts were designed with the following strategies:

Information Collection Prompts: Simple, natural questions that simulate recruiter behavior

Dynamic Technical Questions: Prompt templates query LLMs to generate questions based on user-input tech stack and position

Fallback Handling: In case of API failure, hardcoded rules are used to generate meaningful questions locally

Context-Aware Chat: Maintains state between turns to make the conversation feel smooth and intelligent

🧩 Challenges & Solutions
Challenge	Solution
API errors like unauthorized or quota exceeded	Added fallback logic to generate predefined questions
Maintaining conversation state across turns	Built a HiringAssistant class to manage stage-wise logic
Handling various tech stack inputs	Used normalization and set-based matching
Designing a real chat-like UI in Streamlit	Used st.session_state and message lists to simulate chat flow
Avoiding overwhelming the user with all questions at once	Switched to a one-by-one questioning loop

📬 Feedback
If you'd like to suggest improvements or report issues, feel free to open an issue or contact the developer.

