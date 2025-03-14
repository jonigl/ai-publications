# Ollama with Python Examples

This directory contains Python examples to demonstrate using Ollama with Python.

## Prerequisites

1. Make sure [Ollama](https://ollama.com/) is installed and running on your system.
2. Pull the required models:
   ```
   ollama pull llama3.2:1b
   ```

## Setup

1. Create a virtual environment:
   ```
   # Create the virtual environment
   python -m venv ollama-env

   # Activate the environment
   # On Windows:
   ollama-env\Scripts\activate
   # On macOS/Linux:
   source ollama-env/bin/activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Available Examples

### 1. Basic Usage (basic.py)
Simple example generating a complete response:
```
python basic.py
```

### 2. Streaming Response (streaming.py)
See the response as it's being generated:
```
python streaming.py
```

### 3. Using System Prompts (system-role.py)
Example of using a system prompt to set model behavior:
```
python system-role.py
```

### 4. Conversation Context (conversation-context.py)
Interactive chat example that maintains conversation history:
```
python conversation-context.py
```
Type 'exit' to end the conversation.

## Notes

- These examples use the `llama3.2:1b` model, which is relatively small and fast.
- Make sure Ollama is running in the background before executing these scripts.
- For more details, refer to the [main article](../README.md).
