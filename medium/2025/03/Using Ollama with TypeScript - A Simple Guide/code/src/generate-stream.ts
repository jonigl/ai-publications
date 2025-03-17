import { Ollama } from "ollama";

async function main() {
  const ollama = new Ollama();
  
  console.log("Streaming response:");
  
  // Streaming response
  const stream = await ollama.generate({
    model: "llama3.2:1b",
    prompt: "Why is the sky blue?",
    stream: true
  });
  
  for await (const chunk of stream) {
    process.stdout.write(chunk.response);
  }
  
  console.log(); // New line at the end
}

main().catch(console.error);
