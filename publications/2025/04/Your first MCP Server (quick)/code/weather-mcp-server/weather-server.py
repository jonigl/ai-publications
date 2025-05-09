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
