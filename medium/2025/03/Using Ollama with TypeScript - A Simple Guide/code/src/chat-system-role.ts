import { Ollama } from "ollama";

async function main() {
  const ollama = new Ollama();
  
  // Define a system prompt
  const systemPrompt = "You speak and sound like a pirate with short sentences.";
  
  // Chat with a system prompt
  const response = await ollama.chat({
    model: "llama3.2:1b",
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: "Tell me about your boat." }
    ]
  });
  
  console.log(response.message.content);
}

main().catch(console.error);
