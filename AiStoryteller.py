from config import API_KEY, ENDPOINT
import speech_recognition as sr
import win32com.client
from openai import AzureOpenAI

speaker = win32com.client.Dispatch("SAPI.SpVoice")


API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-35-turbo"

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

# Global variable to store conversation history
conversation_history = [
    {"role": "system", "content": "You are a bed time story teller assistant for child which is created by Ayush. your main work is to ask the preferences like themes from the child and based on the theme create a good and long story. you are only allowed to ask small question and generate large storys."}
]


def get_user_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Recording complete")

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio, language="en-in")
        # user_input = input('user : ')
        print("YOU : " + user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio")
        return "Sorry, I did not understand the audio"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return f"Could not request results; {e}"
    except Exception as e:
        print(f"Some Error Occurred: {e}")
        return f"Some Error Occurred: {e}"


def generate_response():
    global conversation_history
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=conversation_history,
    )
    response = completion.choices[0].message.content
    return response


def main():
    global conversation_history
    print("My name is Ayush Kumar and I am participating in the Microsoft Developer AI Learning Hackathon. Can you tell me which type of story would you like to hear?")
    speaker.Speak("My name is Ayush Kumar and I am participating in the Microsoft Developer AI Learning Hackathon. Can you tell me which type of story would you like to hear?")
    print("Say 'exit' to quit.")
    while True:
        user_input = get_user_input()
        if user_input.lower() == 'exit':
            print("Exiting...")
            speaker.Speak("Thanks for using the AI-powered bedtime storyteller created by Ayush Kumar.")
            break
        elif user_input.lower() == '':
            continue
        conversation_history.append({"role": "user", "content": user_input})
        response = generate_response()
        print("Assistant:", response)
        speaker.Speak(response)
        conversation_history.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
