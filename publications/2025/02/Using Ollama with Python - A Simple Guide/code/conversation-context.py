from ollama import chat

# Initialize an empty message history
messages = []
while True:
    user_input = input('Chat with history: ')
    if user_input.lower() == 'exit':
        break
    # Get streaming response while maintaining conversation history
    response_content = ""
    for chunk in chat(
        'llama3.2:1b',
        messages=messages + [
            {'role': 'system', 'content': 'You are a helpful assistant. You only give a short sentence by answer.'},
            {'role': 'user', 'content': user_input},
        ],
        stream=True
    ):
        if chunk.message:
            response_chunk = chunk.message.content
            print(response_chunk, end='', flush=True)
            response_content += response_chunk
    # Add the exchange to the conversation history
    messages += [
        {'role': 'user', 'content': user_input},
        {'role': 'assistant', 'content': response_content},
    ]
    print('\n')  # Add space after response
