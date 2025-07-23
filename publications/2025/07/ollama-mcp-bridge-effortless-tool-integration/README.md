# Ollama MCP Bridge: Effortless Tool Integration

![cover](./img/ollama-mcp-bridge-cover.jpg)

> **_TL;DR:_**_
> Ollama MCP Bridge is a lightweight, drop-in proxy that transparently adds every MCP server tool to your Ollama chat completions_

# The Spark & Inspiration

When I first started experimenting with Ollama’s REST API, I was amazed by how effortlessly it spun up local LLMs, and yet real-world AI apps need more. Calls to external “tools” (weather services, file systems, analytics engines , etc) are essential, but integrating MCP servers into an Ollama-based workflow still meant integrating an MCP SDK and writing custom code.

As the creator of  [mcp-client-for-ollama](https://github.com/jonigl/mcp-client-for-ollama)  (a Model Context Protocol client for Ollama), I experienced this friction firsthand. The discussion in  [GitHub issue #22](https://github.com/jonigl/mcp-client-for-ollama/issues/22)  crystallized the need for a simpler, zero‑boilerplate solution:

> _“Integrating MCP tools into Ollama chat flows currently requires manual glue logic and custom middleware . There must be a simpler way!”_

That moment sparked  **Ollama MCP Bridge**, a true drop‑in proxy that automatically discovers, aggregates, and injects all MCP tools into every  `/api/chat`  request without any extra code, while proxying other endpoints unchanged.

# Introducing Ollama MCP Bridge

Ollama MCP Bridge is a  **FastAPI**-powered  **proxy**  that you install between your client and your Ollama server. It:

1.  **Loads**  your MCP server configurations from a simple JSON file
2.  **Collects**  all exposed tool definitions at startup
3.  **Proxies**  all non-chat endpoints directly to Ollama, unchanged
4.  **Intercepts**  `/api/chat`  calls, injects the full tool list, and orchestrates any tool invocations
5.  **Streams**  both “thinking” messages and final responses, just like plain Ollama

All you need to do is run:

uvx ollama-mcp-bridge
# or if you prefer installing it
pip install --upgrade ollama-mcp-bridge
ollama-mcp-bridge --config /path/to/mcp-config.json

Point your client at  `http://localhost:8000`  instead of your Ollama server, and voilà! every  **chat completion**  now has all your  **MCP server tools**  available.

# Quickstart Example

1.  **Create your MCP config**  at  `mcp-config.json`:

{
  "weather": {
    "command": "python",
    "args": [
      "mock-weather-mcp-server.py"
    ]
  },
  "filesystem": {
    "command": "npx",
    "args": [
      "@modelcontextprotocol/server-filesystem",
      "/tmp"
    ]
  }
}

> The mock-weather-mcp-server.py MCP Server is provided within the  [repo](https://github.com/jonigl/ollama-mcp-bridge/tree/main/mcp-servers-config)

**2. Launch the bridge**:

ollama-mcp-bridge --config mcp-config.json --host 0.0.0.0 --port 8000

**3. Call the chat API**:

curl -N -X POST http://localhost:8000/api/chat -H "accept: application/json" -H "Content-Type: application/json" -d '{
    "model": "qwen3:0.6b",
    "messages": [
      {
        "role": "system",
        "content": "You are a weather assistant."
      },
      {
        "role": "user",
        "content": "What is the weather like in Paris today?"
      }
    ],
    "think": false,
    "stream": false,
    "options": {
      "temperature": 0.7,
      "top_p": 0.9
    }
  }'

> You can optionally use (pipe)  `[jq](https://jqlang.org/)`  for better readability

And you will receive and response like this one:

{
  "model": "qwen3:0.6b",
  "created_at": "2025-07-22T23:25:04.50262Z",
  "message": {
    "role": "assistant",
    "content": "The current temperature in Paris is 19°C. It is quite mild and pleasant, with a comfortable climate for a day in the city."
  },
  "done_reason": "stop",
  "done": true,
  "total_duration": 564504625,
  "load_duration": 59264417,
  "prompt_eval_count": 55,
  "prompt_eval_duration": 50007792,
  "eval_count": 30,
  "eval_duration": 452835041
}

Behind the scenes, Ollama MCP Bridge will expose both weather and filesystem tools. So you could also ask it to list your /tmp directory or run custom analyses without changing your client code.

> If you want a simple Ollama chat web client, check out  [simple-ollama-chat](https://github.com/jonigl/simple-ollama-chat).

# Under the Hood: How It Works

**1. Startup**

-   Reads  `mcp-config.json`, which lists one or more MCP servers and how to launch them.
-   Spawns or connects to each server, fetches their tool schemas.

**2. Tool Aggregation**

-   Builds a unified list of tools (name, description, JSON schema) from all MCP servers.

**3. Chat Proxying**

-   On  `POST /api/chat`: merges the tool list into the request payload under  `tools`.
-   Streams messages from Ollama, watches for any tool calls.

**4. Tool Execution**

-   When Ollama invokes a tool: the bridge forwards the call to the appropriate MCP server, waits for its JSON response, then feeds it back into the chat stream as another message.

**5. Other Endpoints**

-   `/health`,  `/models`,  `/completions`, etc., are simply forwarded to your Ollama server—unchanged and unburdened.

Under the hood,  [**FastAPI**](https://fastapi.tiangolo.com/)  handles asynchronous streams and WebSocket-style interactions, while  [loguru](https://github.com/Delgan/loguru)  gives you rich, structured logs for debugging.

# Why You’ll Love It

-   🚀  **Zero Boilerplate:**  No more writing custom middleware for each new tool.
-   🔧  **Config-Driven:**  Add or remove MCP servers simply by editing JSON. No code changes needed.
-   🔄  **Streaming “Thinking” Messages:**  Keep your UX snappy with incremental updates.
-   🔌  **Full Ollama Compatibility:**  Use any existing Ollama client or library. Just point it at this bridge.
-   📦  **PyPI & UVX:**  Install with a single command, or pull from source if you want to hack on it.

# Try It Today

Ollama MCP Bridge is available on  **GitHub**  and  **PyPI**:

-   🔗  **GitHub**:  [https://github.com/jonigl/ollama-mcp-bridge](https://github.com/jonigl/ollama-mcp-bridge)
-   📦  **PyPI**:  [https://pypi.org/project/ollama-mcp-bridge/](https://pypi.org/project/ollama-mcp-bridge/)

I’d love to hear how you’re using it so feel free to drop a comment below.

> If you enjoyed this article, please leave a star ⭐️ on the GitHub repo of the Ollama MCP Bridge project. Thank you for your support.
>
>![GitHub Repo stars](https://img.shields.io/github/stars/jonigl/ollama-mcp-bridge?style=social&link=https%3A%2F%2Fgithub.com%2Fjonigl%2Follama-mcp-bridge)
