


from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")  
)


def decompose_task(user_request):
    prompt = f"""
    You are an AI task planner. Break the User request into smaller tasks. 
    Rules:
    1. Create only the tasks necessary to complete the request.
    2. Put the tasks in the correct execution order.
    3. Each task should be a short action.
    4. Return one task per line.
    5. Do not number the task.
    6. Do not explain anything.
    
    User Request : {user_request}
    
    """
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[{
            "role":"system",
            "content":"You are an AI task planner"
        },
        {
            "role":"user",
            "content":prompt
        }
        ]
    )

    result  = response.choices[0].message.content.strip()
    task = []
    for line in result.splitlines():
        line = line.strip()
        if line:
            task.append(line)
    return task

  