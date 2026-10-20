import asyncio
from agent.mcp_client.mcp_client import *


async def main ():
    client = await connect()
    tools = await discover_tools(client)
    # print(f"{tools}")
    for tool in tools :
        print(f"{tool.name}")

        result = await execute_tool(
            client,
            tool.name
            )
        print(f"{result.content[0].text}")

asyncio.run(main())