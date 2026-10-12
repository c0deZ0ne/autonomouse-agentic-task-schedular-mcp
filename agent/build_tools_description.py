def build_tool_descriptions(tools):
    description = ''
    for tool in tools:
        description += f"""
            "Tool":{tool.name},
            "Description":{tool.description}
        """

    return description

