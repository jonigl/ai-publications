# Ollama with TypeScript Examples

This directory contains TypeScript examples to demonstrate using Ollama with TypeScript.

## Prerequisites

1. Make sure [Ollama](https://ollama.com/) is installed and running on your system.
2. Pull the required models:
   ```
   ollama pull llama3.2:1b
   ```
3. Ensure you have Node.js (v18 or higher recommended) installed.

## Setup

1. Install dependencies:
   ```
   npm install
   ```

2. Run examples using npm scripts:
   ```
   npm run basic
   npm run stream
   npm run system-role
   npm run chat
   ```

   Or directly with tsx:
   ```
   npx tsx src/generate.ts
   ```

## Available Examples

### 1. Basic Usage (src/generate.ts)
Simple example generating a complete response:
```
npx ts-node src/generate.ts
```

### 2. Streaming Response (src/generate-stream.ts)
See the response as it's being generated:
```
npx ts-node src/generate-stream.ts
```

### 3. Using System Prompts (src/chat-system-role.ts)
Example of using a system prompt to set model behavior:
```
npx ts-node src/chat-system-role.ts
```

### 4. Conversation Context (src/chat-history-stream.ts)
Interactive chat example that maintains conversation history:
```
npx ts-node src/chat-history-stream.ts
```
Type 'exit' to end the conversation.

## Notes

- These examples use the `llama3.2:1b` model, which is relatively small and fast.
- Make sure Ollama is running in the background before executing these scripts.
- For more details, refer to the [main article](../README.md).
