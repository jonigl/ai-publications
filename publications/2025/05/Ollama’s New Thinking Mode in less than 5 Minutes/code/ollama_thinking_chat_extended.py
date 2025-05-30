import argparse
import asyncio
import ollama
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown

THINKING_MODELS = ["deepseek-r1", "qwen3"]

class OllamaThinkingClient:
    def __init__(self, model: str = "qwen3:0.6b"):
        self.console = Console()
        self.model = model
        self.ollama = ollama.AsyncClient()
        self.messages = [{"role": "system", "content": "You are a helpful assistant that thinks through answers."}]

    async def validate_model(self):
        """Check if the model is available and supports thinking"""
        try:
            models = await self.ollama.list()
            available_models = [m["model"] for m in models.get("models", [])]
            thinking_models = [m for m in available_models if m.split(":")[0] in THINKING_MODELS]

            if self.model not in thinking_models:
                self.console.print(f"[red bold]Model '{self.model}' is not a thinking model.[/red bold]")

                if thinking_models:
                    self.console.print("[green bold]Available thinking models:[/green bold]")
                    for model in thinking_models:
                        self.console.print(f"[green]- {model}[/green]")
                else:
                    self.console.print("[red]No thinking models found. Install with:[/red]")
                    self.console.print("[yellow]ollama pull deepseek-r1[/yellow] or [yellow]ollama pull qwen3[/yellow]")

                return False
            return True
        except Exception as e:
            self.console.print(f"[red]Error checking models: {e}[/red]")
            return False

    async def process_query(self, query: str):
        """Send query to model and display the streaming response"""
        self.messages.append({"role": "user", "content": query})
        response = await self.ollama.chat(
            model=self.model,
            messages=self.messages,
            stream=True,
            think=True
        )

        thinking_content = ""
        answer_content = ""
        thinking_started = False

        with Live(console=self.console, refresh_per_second=10, vertical_overflow='visible') as live:
            async for chunk in response:
                message = chunk['message']

                # Handle thinking content
                if message.get('thinking'):
                    if not thinking_started:
                        thinking_content = "🤔 **Thinking:**\n\n"
                        thinking_started = True
                    thinking_content += message['thinking']
                    live.update(Markdown(thinking_content, style="dim"))

                # Handle answer content
                if message.get('content'):
                    answer_content += message['content']
                    live.update(Markdown(answer_content))
        if answer_content:
            self.messages.append({"role": "assistant", "content": answer_content})

    async def chat_loop(self):
        """Main chat loop for user interaction"""
        self.console.print(f"[bold green]🤖 Ollama Thinking Client[/bold green] [cyan]({self.model})[/cyan]")
        self.console.print("[yellow]Type your questions or 'quit' to exit[/yellow]\n")

        while True:
            try:
                query = self.console.input("[bold blue]🔹Query:[/bold blue] ").strip()
                if query.lower() in ['quit', 'exit', 'q']:
                    self.console.print("[yellow]Goodbye! 👋[/yellow]")
                    break
                if query:
                    await self.process_query(query)
                    self.console.print()  # Add spacing after response
            except (KeyboardInterrupt, EOFError):
                self.console.print("\n[yellow]Goodbye! 👋[/yellow]")
                break
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")

async def main():
    parser = argparse.ArgumentParser(description="Ollama Thinking Client - Chat with models that show their reasoning")
    parser.add_argument(
        "--model",
        default="qwen3:0.6b",
        help="Thinking model to use (e.g., 'deepseek-r1', 'qwen3')"
    )
    args = parser.parse_args()

    client = OllamaThinkingClient(model=args.model)

    # Validate model before starting
    if await client.validate_model():
        await client.chat_loop()

if __name__ == "__main__":
    asyncio.run(main())
