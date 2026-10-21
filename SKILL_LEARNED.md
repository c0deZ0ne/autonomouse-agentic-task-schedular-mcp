# Technical Skills Learned

This document summarizes the practical technical skills developed during the AI-agent training represented in this repository. Each skill is supported by an exercise or implementation in the codebase.

## Python Programming

- Writing reusable functions and organizing code into modules
- Working with dictionaries, lists, loops, conditionals, and type hints
- Reading local files and navigating paths with `pathlib`
- Handling configuration through environment variables and `.env` files
- Using `async` and `await` for asynchronous workflows
- Generating secure random values with Python's `secrets` module
- Importing and using third-party packages in a virtual environment

## Generative AI and LLM APIs

- Configuring and using the OpenAI Python SDK
- Sending system and user messages to a chat-completion model
- Reading model names, API keys, and base URLs from environment variables
- Writing focused prompts for planning, task decomposition, and answer generation
- Parsing model output into application-friendly Python data
- Running local language and embedding models with Ollama

## AI Agent Development

- Building a planner-executor agent architecture
- Creating an iterative agent loop with explicit stopping conditions
- Tracking requests, actions, observations, step counts, and final answers
- Using previous observations to guide the agent's next action
- Preventing unlimited execution with a maximum-step guard
- Separating planning, execution, state management, and response formatting
- Decomposing a multi-part request into small, ordered tasks with an LLM

## Model Context Protocol (MCP)

- Creating an MCP server with FastMCP
- Exposing Python functions as tools with the `@mcp.tool()` decorator
- Connecting an asynchronous MCP client to a server over standard input/output
- Discovering available tools dynamically at runtime
- Calling tools by name and reading their returned content
- Providing tool names and descriptions to an LLM planner

## Retrieval and Embeddings

- Building a small file-based knowledge base
- Implementing basic keyword retrieval
- Generating text embeddings with an OpenAI-compatible embedding API
- Representing text as numerical vectors
- Calculating cosine similarity with NumPy
- Comparing semantic similarity between pieces of text

## Software Engineering Practices

- Structuring a project into components with separate responsibilities
- Protecting credentials by loading them from environment variables
- Using Git and GitHub for source control and portfolio presentation
- Writing small component tests and executable experiments
- Debugging model configuration, imports, and client-server communication
- Documenting setup, architecture, limitations, and future improvements

## Libraries and Tools Used

- Python
- OpenAI Python SDK
- FastMCP
- NumPy
- `python-dotenv`
- Ollama
- Git and GitHub
- PowerShell and command-line tools

## Practical Evidence

| Skill area | Evidence in this repository |
| --- | --- |
| Agent loop and state | `agent/loop.py`, `agent/agent_state.py` |
| LLM planning | `agent/planner.py` |
| Task decomposition | `agent/decompose_task.py` |
| Tool execution | `agent/executor.py` |
| MCP client/server | `agent/mcp_client/`, `agent/mcp_server/` |
| Response generation | `agent/format_answer.py` |
| Retrieval and embeddings | `Day06_P4/` |
| Utility functions | `tools.py` |

## Current Learning Level

These projects demonstrate foundational, hands-on experience with Python AI agents and tool integration. The repository is a learning portfolio, not yet a production system. Important next areas include structured tool arguments, stronger automated testing, input validation, logging, dependency pinning, and production error handling.
