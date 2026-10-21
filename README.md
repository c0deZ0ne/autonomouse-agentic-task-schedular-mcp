# AI Agent Learning Portfolio

An educational Python repository that follows the development of an AI agent from basic retrieval and embeddings to a stateful, tool-using agent built with the Model Context Protocol (MCP).

The current agent can discover tools from a local MCP server, ask a language model to select the next action, execute the selected tool, save observations, and turn the results into a natural-language response.

## What I Built

- A keyword-based document retriever for a small local knowledge base
- Embedding experiments using Ollama and `nomic-embed-text`
- Cosine-similarity calculation with NumPy
- A planner–executor agent loop with a configurable step limit
- Agent state tracking for actions, observations, and final answers
- An MCP server with time, password-generation, and dice-rolling tools
- An asynchronous MCP client for connecting, discovering tools, and invoking them
- An LLM-based task decomposer that converts multi-part requests into ordered actions
- Small tests and learning exercises for individual components

## Skills Gained

### Python development

- Functions, modules, imports, dictionaries, and type hints
- File handling with `pathlib`
- Exception handling and environment variables
- Asynchronous programming with `async` and `await`
- Secure random-value generation with Python's `secrets` module

### AI and language models

- Calling OpenAI-compatible chat and embedding APIs
- Running local models through Ollama
- Prompt design for planning and response generation
- Prompt design and output parsing for task decomposition
- Vector embeddings and cosine similarity
- Basic information retrieval and knowledge-base design

### Agent engineering

- Planner–executor architecture
- Iterative agent loops and termination conditions
- State and observation management
- Tool selection, discovery, and execution
- Separation of planning, execution, memory, and answer formatting
- Breaking complex requests into smaller, ordered tasks

### Protocols and software practices

- MCP client/server communication over standard input/output
- Modular project organization and separation of concerns
- Configuration with `.env` files
- Component-level testing and debugging

## Repository Structure

```text
AI-agent-udemy/
|-- agent/
|   |-- main.py                    # Current command-line entry point
|   |-- loop.py                    # Agent control loop
|   |-- planner.py                 # LLM-based next-action selection
|   |-- executor.py                # Tool execution
|   |-- agent_state.py             # State and step management
|   |-- format_answer.py           # Final response generation
|   |-- decompose_task.py          # LLM-based task decomposition exercise
|   |-- mcp_client/mcp_client.py   # MCP connection and tool calls
|   `-- mcp_server/server.py       # Local MCP tools
|-- Day06_P4/                      # Retrieval and embedding exercises
|-- Day09_P2/                      # Earlier agent implementation
|-- tools.py                       # Reusable Python utilities
|-- test_*.py                      # Learning tests and experiments
|-- SKILL_LEARNED.md               # Technical skills and code evidence
`-- ACADEMIC_RESUME_TEMPLATE.md    # Résumé template for internship use
```

## Setup

### 1. Create and activate a virtual environment

PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 2. Install the Python packages

```bash
pip install openai python-dotenv fastmcp numpy
```

### 3. Configure the model

Create or update `.env` in the repository root:

```env
BASE_URL=https://api.openai.com/v1
API_KEY=your_openai_api_key
MODEL=gpt-4o-mini
```

Do not commit real API keys.

For local use with Ollama, install Ollama and pull the models required by the exercises. For example:

```bash
ollama pull qwen3:4b
ollama pull nomic-embed-text
```

Model names must match the names available in your local Ollama installation.

## Run the Agent

From the repository root:

```powershell
python agent\main.py
```

The program starts the MCP server through the client, displays the available tools, and prompts for a request. Example requests include:

```text
What time is it?
Generate a secure password.
Roll two dice.
```

## How the Agent Works

1. `main.py` connects to the MCP server and discovers its tools.
2. `loop.py` creates the initial state and controls each agent step.
3. `planner.py` gives the model the request, tool descriptions, and earlier observations.
4. `executor.py` invokes the tool selected by the planner.
5. The loop records the result and continues until the planner returns `FINISH` or the step limit is reached.
6. `format_answer.py` converts the recorded observations into a user-facing answer.

The separate `decompose_task.py` exercise demonstrates how an LLM can turn a multi-part request into a list of smaller actions. It is not yet connected to the main agent loop.

## Current Limitations

- The planner selects a tool name but does not yet generate tool arguments.
- Task decomposition is currently a standalone prototype and is not integrated into execution.
- The main workflow has limited automated test coverage.
- Some root-level files and dated folders are earlier learning exercises rather than production code.
- Error handling and validation can be strengthened.
- Dependency versions are not yet pinned in a requirements file.

## Suggested Next Steps

- Add planner support for structured tool arguments
- Add unit and integration tests with mocked model responses
- Validate planner output before executing a tool
- Add timeouts and clearer MCP/model error messages
- Create a pinned `requirements.txt` or `pyproject.toml`
- Add logging and conversation history

## Résumé Resource

See [ACADEMIC_RESUME_TEMPLATE.md](ACADEMIC_RESUME_TEMPLATE.md) for an academic résumé format aimed at a software or AI internship. Replace every placeholder and keep only claims you can explain in an interview.

## Training Skills

See [SKILL_LEARNED.md](SKILL_LEARNED.md) for a detailed list of the technical skills earned during the training and the project files that demonstrate each skill.

## Status

This is a learning portfolio and work in progress, not a production-ready agent.
