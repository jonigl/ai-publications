# Ollama Thinking Mode - Code Examples

This directory contains two Python examples demonstrating Ollama's new thinking mode feature introduced in v0.9.0.

## Files

- `ollama_thinking_chat.py` - Basic interactive chat with thinking mode
- `ollama_thinking_chat_extended.py` - Extended version with additional features
- `pyproject.toml` - Project dependencies configuration
- `uv.lock` - Locked dependency versions

## Prerequisites

Before running these examples, make sure you have:

1. **Ollama v0.9.0 or higher** installed
   ```bash
   ollama --version   # should show 0.9.0 or higher
   ```

2. **A thinking-capable model** pulled (we recommend `qwen3:0.6b`)
   ```bash
   ollama pull qwen3:0.6b
   ```

3. **Python 3.10 or higher** and **uv** package manager
   ```bash
   python --version   # should show 3.10 or higher
   uv --version       # install from https://github.com/astral-sh/uv
   ```

## Setup

1. Navigate to this directory:
   ```bash
   cd "Ollama's New Thinking Mode in less than 5 Minutes/code"
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

   Or manually install if you prefer:
   ```bash
   uv add ollama rich
   ```

## Running the Examples

### Example 1: Basic Thinking Chat (`ollama_thinking_chat.py`)

This is the main example from the tutorial - a simple interactive chat that shows the model's thinking process in real-time.

```bash
python ollama_thinking_chat.py
```

**Features:**
- Real-time display of model's thinking process
- Interactive chat interface
- Clean markdown formatting
- Type 'quit' or 'exit' to stop

**Example usage:**
```
Question: What is the capital of France?
Question: Is 5 a Fibonacci number?
Question: How do you make a paper airplane?
```

### Example 2: Extended Thinking Chat (`ollama_thinking_chat_extended.py`)

An enhanced version with additional features and capabilities.

```bash
python ollama_thinking_chat_extended.py
```

**Additional features:**
- Enhanced error handling
- More configuration options
- Extended conversation history
- Better formatting and display

## Troubleshooting

### Common Issues

1. **"Model not found" error**
   ```bash
   ollama pull qwen3:0.6b
   ```

2. **"Connection refused" error**
   - Make sure Ollama is running: `ollama serve`
   - Check if Ollama is installed and accessible

3. **Import errors**
   - Ensure you're in the virtual environment: `source .venv/bin/activate`
   - Reinstall dependencies: `uv sync`

4. **Thinking mode not working**
   - Verify you have Ollama v0.9.0+: `ollama --version`
   - Ensure you're using a thinking-capable model like `qwen3:0.6b`

### Performance Tips

- Use `qwen3:0.6b` for fastest responses (recommended for this demo)
- For more complex reasoning, try larger thinking-capable models
- Adjust `refresh_per_second` in the code for different streaming speeds

## What You'll See

When you run either example, you'll see:

1. **Thinking Phase** (dimmed text): The model's internal reasoning process
2. **Final Answer** (normal text): The clean, final response

The thinking process reveals how the model:
- Breaks down complex problems
- Considers multiple approaches
- Arrives at its final answer

## Next Steps

After trying these examples, you can:

- Modify the system prompts for different behaviors
- Experiment with different thinking-capable models
- Build your own applications using the thinking mode API
- Integrate thinking mode into existing Ollama applications

## Resources

- [Ollama Documentation](https://ollama.com/)
- [Ollama Python SDK](https://github.com/ollama/ollama-python)
- [Rich Library Documentation](https://rich.readthedocs.io/)

Enjoy exploring AI transparency with Ollama's thinking mode! 🤔💭
