import asyncio
from mcp_client.mcp_client import connect,discover_tools,disconnect
from loop import  run_agent_loop
from  format_answer import format_answer
from executor import execute_action
from planner import planner
async def main ():
    client = await connect()
    tools = await discover_tools(client)
    print("\nAvailableTools\n\n-------------------")

    for tool in tools:
        print(tool.name) 

    user_request=input("\nUser :")

    state = await run_agent_loop(
        user_request,
        planner,
        execute_action,
        format_answer,
        tools,
        client
    )

    print("\nFinal Answer: ")
    print(state)

    await disconnect(client)

if __name__ == "__main__":
    asyncio.run(main())
