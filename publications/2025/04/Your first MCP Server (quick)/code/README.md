# Weather MCP Server Example

A simple MCP (Model Context Protocol) server that provides a weather tool for LLMs to use.

## Usage Options

You have two ways to use this project:

1. **Follow the step-by-step instructions below** to create your own weather MCP server from scratch.
2. **Use the pre-generated code** in the [weather-mcp-server](./weather-mcp-server) directory where all the files are already set up for you.

If using the pre-generated code, just navigate to that directory and proceed from step 5 (Testing with Ollama).

## Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) for Python package management
- [Ollama](https://ollama.com/) (if you want to test with a local LLM)

## Setup Instructions

### 1. Install uv (if not already installed)

Follow the [official installation instructions](https://github.com/astral-sh/uv?tab=readme-ov-file#installation).

### 2. Create and setup the project

```bash
# Create a new project
uv init weather-mcp-server
cd weather-mcp-server

# Add the MCP dependency
uv add "mcp[cli]"

# Create the server file
touch weather-server.py
```

### 3. Write the Weather MCP Server

Copy this code into `weather-server.py`:

```python
# FastMCP is all what we need from mcp dependency  
from mcp.server.fastmcp import FastMCP  
# We will use this lib to request the weather from wttr.in   
import urllib  
  
# Now lets create an MCP Server  
mcp = FastMCP("Weather")  
  
# Now let's register a tool with this decorator,   
@mcp.tool()  
def get_weather(city: str) -> str: # define a function with city argument  
  # And now we will docuement this cuntion using Python Docstrings  
  # FastMCP will add this documentation to the LLM so it can decide when to use  
  # this tool and how to use it.  
  """  
  Get the current weather for a given city  
  Args:  
    city (str): The name of the city  
  Returns:  
    str: The current weather in the city, for example, "Sunny +20°C"  
  """  
  try:  
    # URL-encode the city name.  
    url_encoded_city = urllib.parse.quote_plus(city)  
    # Prepare wittr url request  
    wttr_url = f'https://wttr.in/{url_encoded_city}?format=%C+%t'  
    # Request weather  
    response = urllib.request.urlopen(wttr_url).read()    
    return response.decode('utf-8')  
  except Exception as e:  
    # If something goes wrong we let the LLM know about it  
    return f"Error fetching weather data"  
  
# And here we add the main entry point for the server  
if __name__ == "__main__":  
  # Here we initialize and run the server  
  # We select stdio transport for process-based communication.   
  # This allow a process (the client) to communicate with its parent   
  # process through pipes using standard input/output.  
  mcp.run(transport='stdio')
```

### 4. Create the MCP servers configuration file

Create a file named `mcp-servers-config.json` with the following content:

```json
{  
  "mcpServers": {  
    "weather": {  
      "command": "uv",  
      "args": [  
        "--directory",  
        ".",  
        "run",  
        "weather-server.py"  
      ]  
    }  
  }  
}
```

**Important Note**: This configuration uses `"--directory", "."` which means `ollmcp` must be run from within the project directory. This relative path approach is more portable than using absolute paths.

### 5. Test with Ollama using ollmcp

#### Install Ollama
If you haven't already, [install Ollama](https://ollama.com/download).

#### Pull a model that supports tools
```bash
ollama pull qwen2.5:7b
```

#### Install the ollmcp client
```bash
pip install ollmcp
```

#### Run the MCP client
Make sure you're in the weather-mcp-server directory, then run:
```bash
ollmcp --servers-json mcp-servers-config.json --model qwen2.5:7b
```

### 6. Try it out!

When the client is running, try asking a question like:
- "What's the weather in New York City?"
- "How's the weather in Tokyo today?"
- "Tell me about the current weather in Paris"

The LLM will use your MCP weather tool to fetch and display the current weather information.

## Troubleshooting

- If you encounter directory issues when running `ollmcp`, make sure you're running the command from within the project directory where the `mcp-servers-config.json` file is located.
- Ensure you have internet access, as the weather tool fetches data from wttr.in.
- If the LLM isn't using the tool, try rephrasing your question to be more explicitly about the weather.

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/introduction)
- [ollmcp GitHub Repository](https://github.com/jonigl/mcp-client-for-ollama)
- [wttr.in Weather Service](https://wttr.in/)
