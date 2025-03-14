from ollama import generate  
# Streaming response  
print("Streaming response:")  
for chunk in generate('llama3.2:1b', 'Why is the sky blue?', stream=True):  
    print(chunk['response'], end='', flush=True)  
print() # New line at the end
