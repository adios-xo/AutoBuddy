greeting1 = ["hi", "hey", "hello", "greetings", "yo", "sup"]
greeting2 = ["good morning", "good afternoon", "good evening"]
greeting3 = ["how are you", "how you doing", "what's up", "what's good"]


def checkHamilton(text: str):
    if "hamilton" in text.lower():
        return True


def checkGreeting(text: str):
    lowerText = text.lower()

    if lowerText == "hamilton":
        return "Yes, how may I help you?"

    else:
        if any(greet in lowerText for greet in greeting3):
            return "I am good. How may I help you?"

        elif any(greet in lowerText for greet in greeting2):
            for greet in greeting2:
                if greet in lowerText:
                    return f"{greet.capitalize()}. How may I help you?"

        elif any(greet in lowerText for greet in greeting1):
            return "Hey there! How may I help you?"

        else:
            return False
