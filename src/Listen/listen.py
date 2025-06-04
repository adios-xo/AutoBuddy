import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        try:
            print("Speak...")
            
            audio = recognizer.listen(source, timeout=10)

            text = recognizer.recognize_google(audio)

            return text

        except Exception as e:
            return f"some exception occured : {e}"
