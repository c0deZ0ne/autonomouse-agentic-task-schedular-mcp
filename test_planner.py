from openai import OpenAI
# from similarity import cosine_similarity
from dotenv import load_dotenv
from planner import choose_tool
import os
load_dotenv()
client = OpenAI (
    base_url= os.getenv("BASE_URL"),#http://localhost:11434/v1",
    api_key=os.getenv("API_KEY")# "ollama"
)
while True:
    use_ask = input("User: ")
    if use_ask =="exit":
        break
    response = client.chat.completions.create(
        model= "Qwen3:4b",
        messages=[
            {
                "role":"system",
                "content":"You are an AI planner"
            },
            {
                "role":"user",
                "content": choose_tool(use_ask)
            }
    ])


    print(f" Ai Tool choose: {response.choices[0].message.content.strip()}")