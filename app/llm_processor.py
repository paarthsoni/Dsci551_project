import os
import json
from dotenv import load_dotenv
from google import generativeai as genai

load_dotenv()

class CustomGenAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def ask_ai(self, prompt_text):
        try:
            response = self.model.generate_content(prompt_text)
            return response.text
        except Exception as e:
            print("Gemini Error:", e)
            return "Error: Could not generate query."


def clean_code_response(text):
    """
    Removes markdown-style ```python ``` code blocks if present.
    """
    if text.startswith("```"):
        lines = text.splitlines()
        lines = [line for line in lines if not line.strip().startswith("```")]
        return "\n".join(lines).strip()
    return text.strip()


def parse_nl_query(nl_query, db_type):
    """
    Converts a natural language query to SQL or MongoDB query using Gemini API.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY not found in environment."

    
    if db_type == "mysql":
        prompt = f"""
You are a SQL generator. Use the exact schema provided below and return a valid MySQL query.

SCHEMA:
Table: employees(employee_id, name, department_id)
Table: departments(department_id, name)
Table: projects(project_id, employee_id, title)

Rules:
- Only use the columns and table names exactly as shown above.
- Do not guess column names.
- Only return the raw SQL query.
- Do not include any explanation or wrap the output in code blocks.

Query: "{nl_query}"
"""
    else:
       prompt = f"""
You are a MongoDB assistant. Convert the following natural language query into a valid PyMongo expression using Python syntax.

Use the existing variable `db` (already defined) and access collections like `db.employees`, `db.departments`, and `db.projects`.

Schema:
- employees(employee_id, name, department_id)
- departments(department_id, name)
- projects(project_id, employee_id, title)

Do NOT include any import statements.
Do NOT wrap the code in code blocks.
Only return a single executable Python expression or statement using `db`.

Query: "{nl_query}"
"""


    ai = CustomGenAI(api_key)
    raw_result = ai.ask_ai(prompt)
    return clean_code_response(raw_result)
