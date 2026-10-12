from mcp_client.mcp_client import execute_tool

###
# the agent loop doesn't directly know how MCP works. it just simply ask execute_action() to execute the selected action
###
async def execute_action(action,state,client):
    result = await execute_tool(
        client,action
    )
    if hasattr(result,"content"):
        ### this ask:Does the result object have a content attribute ? ###
        ### MCP tool results commonly contain their content actual output inside content ###
        if (result.content):
            return result.content[0].text
        return str(result)