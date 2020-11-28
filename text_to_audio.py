import pyttsx3


def text_to_speech(text=""):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()


if __name__ == '__main__':
    user_input = input("Enter your text: ")
    text_to_speech(user_input)
