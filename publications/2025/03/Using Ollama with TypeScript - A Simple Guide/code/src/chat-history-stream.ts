import { Ollama } from "ollama";
import * as readline from "readline";

async function main() {
  const ollama = new Ollama();
  
  // Initialize an empty message history
  const messages: Array<{ role: string, content: string }> = [];
  
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  const askQuestion = () => {
    rl.question("Chat with history: ", async (userInput) => {
      if (userInput.toLowerCase() === "exit") {
        rl.close();
        return;
      }
      
      // Get streaming response while maintaining conversation history
      let responseContent = "";
      
      const stream = await ollama.chat({
        model: "llama3.2:1b",
        messages: [
          ...messages,
          { role: "system", content: "You are a helpful assistant. You only give a short sentence by answer." },
          { role: "user", content: userInput }
        ],
        stream: true
      });
      
      for await (const chunk of stream) {
        if (chunk.message) {
          const responseChunk = chunk.message.content;
          process.stdout.write(responseChunk);
          responseContent += responseChunk;
        }
      }
      
      // Add the exchange to the conversation history
      messages.push(
        { role: "user", content: userInput },
        { role: "assistant", content: responseContent }
      );
      
      console.log("\n"); // Add space after response
      askQuestion();
    });
  };
  
  askQuestion();
}

main().catch(console.error);
