from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport

import string

async def connect():
    """Connect to the MCP server """
    server_path = Path(__file__).resolve().parent.parent / "mcp_server" / "server.py"
    project_root = server_path.parent.parent
    transport = PythonStdioTransport(
        server_path,
        cwd=str(project_root),
        log_file=server_path.parent / "server-debug.log",
    )
    client = Client(transport)
    await client.__aenter__()
    print ("Connected to MCP Server")
    return client


async def disconnect(client:Client):
    """Disconnect from a server and clean connection """
    await client.__aexit__(
        None,
        None,
        None
    )


async def discover_tools(client:Client):
    tools = await client.list_tools()
    return tools

async def execute_tool(client:Client,tool_name:str,arguments=None):
    """Execute a given tool"""
    if arguments == None :
        arguments={}
    return await client.call_tool(tool_name,arguments)