from decompose_task import decompose_task
user_request = "Generate a password and tell me the current time and explain python"
tasks = decompose_task(user_request)
print("\nGenerated Tasks\n----------------")
for task in tasks:
    print(f"\n{task}")

