
# Getting Started with Ollama: Run LLMs on Your Computer

![](img/cover.webp)

Ollama makes it easy to run large language models (LLMs) locally on your own computer. This simple guide will show you how to install Ollama, run your first model, and use it in a Python script.

# Installing Ollama

# macOS

1.  Download the installer from  [ollama.ai](https://ollama.ai/)
2.  Open the downloaded file and drag Ollama to your Applications folder
3.  Open Ollama from your Applications

# Windows

1.  Download the installer from  [ollama.ai](https://ollama.ai/)
2.  Run the .exe file and follow the installation wizard
3.  Ollama will start automatically when installation completes

# Linux

1.  Just run this
```
curl -fsSL https://ollama.ai/install.sh | sh
```
# Docker

Ollama is also available as a Docker container:
```
docker pull ollama/ollama  
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
# Running Your First Model

Let’s try Llama 3.2 1B, a compact but capable model:
```
ollama run llama3.2:1b
```
The first time you run this command, Ollama will download the model. Once it’s ready, you’ll see a prompt where you can start chatting:
```
>>> Why is the sky blue?  
The sky appears blue due to a phenomenon called Rayleigh scattering. As sunlight travels through the atmosphere, the shorter blue wavelengths of light are scattered more by air molecules than the longer red wavelengths. This scattered blue light comes to us from all directions in the sky, making the sky appear blue during the day.
```
To exit the Ollama terminal, you can:

-   Type  `/bye`  and press Enter
-   Press Ctrl+D (on macOS/Linux)
-   Press Ctrl+C twice

# Basic Ollama Commands

Here are some useful commands to get you started:
```
# List all your downloaded models  
ollama list
```
```
# Download a model without running it  
ollama pull llama3.2:1b
```
```
# Remove a model you no longer need  
ollama rm llama3.2:1b
```
```
# Get information about a model  
ollama info llama3.2:1b
```
# Next Steps

Once you’re comfortable with the basics, you can try the Ollama Python library to integrate it in your Python applications. Check this article  [Using Ollama with Python: A Simple Guide](../Using%20Ollama%20with%20Python%20-%20A%20Simple%20Guide/README.md).

Enjoy the freedom of running AI locally with Ollama!
