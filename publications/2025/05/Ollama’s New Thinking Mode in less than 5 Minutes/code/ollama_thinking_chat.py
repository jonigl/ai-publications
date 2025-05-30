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
