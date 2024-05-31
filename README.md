# AI-Powered Bedtime Storyteller

custom AI copilot built by following the step-by-step developer guide
link- https://bedtime-storyteller.azurewebsites.net/

## Overview

This project is an AI-powered bedtime storyteller designed to interact with children and create customized bedtime stories based on their preferences. The assistant asks the child for story themes and generates long, engaging stories based on the chosen themes. This project is developed by Ayush Kumar as part of the Microsoft Developer AI Learning Hackathon.

## Features

- **Speech Recognition**: Captures user input through the microphone.
- **Text-to-Speech**: Responds to the user with spoken words.
- **Context-Aware Responses**: Generates stories based on the user's preferences using Azure OpenAI.
- **Conversation History**: Maintains the context of the conversation to provide coherent and relevant responses.

## Requirements

- Python 3.7+
- `speech_recognition` library
- `pywin32` library
- Azure OpenAI API key and endpoint

## Setup

### Install Dependencies

1. **Python Libraries**: Install the required Python libraries by running the following command:
   ```bash
   pip install speechrecognition pywin32 openai pyaudio
   
2. **Azure OpenAI**: Ensure you have an API key and endpoint for Azure OpenAI. You will need to create a `config.py` file to store these values.

