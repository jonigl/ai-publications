import { Ollama } from "ollama";

async function main() {
  const ollama = new Ollama();
  
  // Regular response
  const response = await ollama.generate({
    model: "llama3.2:1b",
    prompt: "Why is the sky blue?"
  });
  
  console.log(response.response);
}

main().catch(console.error);
