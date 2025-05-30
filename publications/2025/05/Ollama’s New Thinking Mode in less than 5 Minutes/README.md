# Ollama’s New Thinking Mode in less than 5 Minutes
![Ollama Thinking Mode Cover](./img/cover.png)

> [!TIP] _Get the most of Ollama’s reasoning models with the new thinking mode._

Ollama `v0.9.0` was just released with support for thinking mode, and today the Python SDK reached parity with `v0.5.0`. This means you can start using this powerful reasoning feature right away to build smarter local AI agents.

## Why this is exciting

**Benefits of Thinking Mode**

- **Improved performance on complex tasks** – thinking before responding leads to more accurate, step‑by‑step answers for reasoning and planning.
- **Better understanding of user instructions** – the model can unpack nuanced prompts and pinpoint key requirements.
- **More creative and informative responses** – by exploring multiple possibilities internally, it surfaces fresh ideas and richer explanations.

## What you will learn

Ollama's new thinking mode allows models to reason through complex tasks before providing a final answer. This is a game-changer for building local AI agents that can think through problems, plan solutions, and provide more accurate responses.

On this tutorial I will guide you through setting up a simple interactive chat application that demonstrates this new feature using the Ollama Python SDK. You’ll see how to pull a thinking‑capable model, install the SDK, and run a chat that reveals the model's thought process in real-time.

## What you will do

- Upgrade to the latest `Ollama` release
- Pull thinking‑ready models (`qwen3:0.6b`)
- Install the brand‑new `Ollama Python SDK`
- Run a fully interactive “thought bubble” chat in your terminal using the `rich` library

## Prerequisites

- `Python 3.10` or higher
- [uv](https://github.com/astral-sh/uv) for Python package management
- [Ollama](https://ollama.com/) version ≥ `v0.9.0`
- A thinking‑capable model like `qwen3:0.6b` pulled from Ollama

> [!NOTE] **Heads‑up:** Only models trained to expose their reasoning support thinking today. Check the _thinking models_ list that Ollama is maintaining.

Let’s get started!

## Step 1 - Let's Upgrade Ollama to v0.9.0

We will need the latest Ollama release to use the thinking mode. If you already have Ollama installed, ensure it is at least version 0.9.0. You can check your version with:

```bash
ollama --version   # should print 0.9.0 or higher
```

If you need to upgrade, you can do so with the following command:

```bash
# If you have the desktop app installed, it will prompt you to update.

# macOS or Linux (Homebrew)
brew upgrade ollama

# Windows
winget upgrade Ollama
```

If you don’t have Ollama installed yet check the official website [https://ollama.com/](https://ollama.com/).

## Step 2 - Pull a thinking‑capable model

We will use the `qwen3:0.6b` model, since it is super small and fast, yet supports thinking mode. You can pull it with the following command:

```bash
ollama pull qwen3:0.6b
```

Let's run one quickly to see the CLI in action:

```bash
ollama run qwen3:0.6b "Is 5 a Fibonacci number?" --think
```

You'll see two distinct sections: first, the dim _Thinking..._ output showing the model's internal reasoning, followed by the clean final answer. Because it is only 0.6B parameters, this tiny model blazes through tokens faster than you can read them 😄

## Step 3 - Install the Python SDK with thinking support

Now let's generate a virtual environment using `uv` and install the latest Ollama Python SDK.

> [!TIP] If you don't have `uv` installed, you can do check the [uv documentation](https://github.com/astral-sh/uv?tab=readme-ov-file#installation).

```bash
# Create a new directory for the demo
mkdir ollama-thinking-demo

# Change into the new directory
cd ollama-thinking-demo

# Create a new virtual environment
uv venv
# Activate the virtual environment
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

Now let's install the latest Ollama Python SDK, which includes support for thinking mode and the `rich` library for pretty terminal output:

```bash
uv add ollama rich
```

> [!Tip] Version 0.5.0 introduces the `think` parameter in both `generate` and `chat` helpers. We are installing rich as well

## Step 4 - Copy‑paste the **ThinkingChat** demo

Create a new file called `ollama_thinking_chat.py` and copy the following code into it:

```python
import asyncio
import ollama
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown


class ThinkingChat:
    def __init__(self, model: str = "qwen3:0.6b"):
        self.console = Console()
        self.model = model
        self.ollama = ollama.AsyncClient()
        self.messages = [{"role": "system", "content": "You are a helpful assistant that thinks through answers."}]

    async def ask(self, question: str):
        """Ask a question and see the model think through the answer"""
        self.messages.append({"role": "user", "content": question})
        response = await self.ollama.chat(
            model=self.model,
            messages=self.messages,
            stream=True,
            think=True  # <-- Enable thinking mode
        )

        thinking = ""
        answer = ""

        with Live(console=self.console, refresh_per_second=8) as live:
            async for chunk in response:
                msg = chunk['message']

                # Show thinking process
                if msg.get('thinking'):
                    if not thinking:
                        thinking = "🤔 **Thinking:**\n\n"
                    thinking += msg['thinking']
                    live.update(Markdown(thinking, style="dim"))

                # Show final answer
                if msg.get('content'):
                    answer += msg['content']
                    live.update(Markdown(answer))
        if answer:
            self.messages.append({"role": "assistant", "content": answer})

    async def chat(self):
        """Simple chat loop"""
        self.console.print(f"[bold green]💭 Thinking Chat[/bold green] [dim]({self.model})[/dim]")
        self.console.print("[yellow]Ask me anything! Type 'quit' to exit.[/yellow]\n")

        while True:
            try:
                question = input("Question: ").strip()
                if question.lower() in ['quit', 'exit']:
                    print("Goodbye! 👋")
                    break
                if question:
                    await self.ask(question)
                    print()  # Add space after response
            except (KeyboardInterrupt, EOFError):
                print("\nGoodbye! 👋")
                break


# Run the chat
if __name__ == "__main__":
    chat = ThinkingChat()
    asyncio.run(chat.chat())
```

Save the file as `ollama_thinking_chat.py` and run it with:

```bash
uv run ollama_thinking_chat.py
```

Now you have a fully interactive chat that shows the model's thought process in real-time! Let's try it out. Type a question like:

```bash
Question: Is 5 a Fibonacci number?
```

You should see the model's thinking process displayed in a dimmed format, followed by the final answer. Check out the demo in action:

[![asciicast](https://asciinema.org/a/721503.svg)](https://asciinema.org/a/721503)


## What you can build next

- **Educational tutors** that teach by example, revealing step‑by‑step logic.
- **Debugging dashboards** that compare the chain‑of‑thought across models.
- **Creative assistants** that brainstorm ideas and show their reasoning.
- **Interactive agents** that explain their decisions in real-time.

Check out the complete code in the [code directory](./code/). There you will find:
* The `ollama_thinking_chat.py` file with the full implementation.
* And the extended version `ollama_thinking_chat_extended.py` with additional features and capabilities.


## Final thoughts

With Ollama's new thinking mode and the Python SDK, you can now build applications that leverage the model's reasoning capabilities. This opens up exciting possibilities for creating more intelligent local AI agents that can think through complex tasks and provide better answers.

**Enjoy building!** If this guide saved you time, consider dropping a ⭐️ on this repository. Thank you for your support, and your feedback shapes the next release.

## Resources

- [Ollama Documentation](https://ollama.com/)
- [Ollama Python SDK](https://github.com/ollama/ollama-python)
- [Rich Library Documentation](https://rich.readthedocs.io/)
