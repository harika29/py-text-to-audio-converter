import pyttsx3


def text_to_speech(text=""):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()


if __name__ == '__main__':
    text_to_speech("Hello Harika, How are you doing?")
