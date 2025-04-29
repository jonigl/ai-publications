# Weather MCP Server

A simple MCP (Model Context Protocol) server that provides weather information as a tool for Large Language Models.

## What is this?

This is a simple Python implementation of a Model Context Protocol (MCP) server that provides a weather tool. The server fetches current weather data from wttr.in when requested by an LLM.

## Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) for Python package management
- [Ollama](https://ollama.com/) for testing with a local LLM model

## Getting Started

1. **Set up the environment**

   Make sure you're in the `weather-mcp-server` directory, then create a virtual environment (optional but recommended):
   
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   uv pip install -e .
   ```

3. **Test the server**

   You need an MCP client to test the server. We'll use [ollmcp](https://github.com/jonigl/mcp-client-for-ollama), which works with Ollama:

   a. First, install ollmcp:
   ```bash
   pip install ollmcp
   ```

   b. Make sure Ollama is installed and pull a model that supports tools:
   ```bash
   ollama pull qwen2.5:7b
   ```

   c. Run the MCP client:
   ```bash
   ollmcp --servers-json mcp-servers-config.json --model qwen2.5:7b
   ```

4. **Try it out**

   Ask the model about the weather in different cities:
   - "What's the weather in New York?"
   - "How's the weather in Tokyo right now?"
   - "Tell me about the current weather in London"

   The LLM will use your weather tool to fetch real-time weather data!

## Understanding the Code

- `weather-server.py` - The main server implementation with the weather tool
- `mcp-servers-config.json` - Configuration file for MCP clients
- `pyproject.toml` - Python project configuration

## Next Steps

- Try adding more weather-related functions (forecast, historical data, etc.)
- Experiment with different LLM models that support tools
- Connect this MCP server to other MCP clients

## Troubleshooting

- If you see connection errors, make sure Ollama is running
- If the tool doesn't activate, try being more specific in your weather queries
- For any command path issues, make sure you're running ollmcp from this directory
