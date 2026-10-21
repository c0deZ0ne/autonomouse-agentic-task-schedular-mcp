
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"),
)
def format_answer (state):
    format_format = f"""
    The user  user asked: {state["user_request"]} 

    Actions performed: {state["actions"]}

    Observations: {state["observations"]}
    Answer the user naturally 
    Do not mention Internal Planning.
    Do not mention state.
    Do not mention tools.
    
    """
    response = client.chat.completions.create(
            model=os.getenv("MODEL", "qwen3:1.7b"),
            messages=[
                {
                    "role": "system",
                    "content": "You are humanoid AI"
                },
                {
                    "role": "user",
                    "content": format_format
                }
            ]
        )
    return (response.choices[0].message.content or "").strip()
