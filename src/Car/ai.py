import asyncio
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise EnvironmentError("Error: GOOGLE_API_KEY environment variable is not set.")

genai.configure(api_key=API_KEY)

# car = {
#     "id": 609,
#     "year": 2004,
#     "company": "Chevrolet",
#     "model": "Aveo",
#     "vin": "5J8TB1H2XCA258898",
# }

# personality = {
#     "id": 19,
#     "personality": "villain",
#     "prompt": "You are a theatrical supervillain who plots world domination but also gives perfect driving directions.",
#     "voice": "en-GB-GeorgeNeural",
#     "tone": "dramatic",
# }

# history = []


async def car_response(text, history, car, personality):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash-lite")

        enhanced_prompt = f"You are a car, a {car}. Your personality is {personality["personality"]}: `You're a sarcastic old-timer who’s sick of modern driving habits`. Make the replies short and crisp. Interact with the user in character and include previous chats in your response.\n\nChat history: {history}\n\nUser: {text}"

        response = await model.generate_content_async(enhanced_prompt)
        return response.text
    except Exception as error:
        return f"An error occurred: {error}"


# async def ai(car, personality, history):
#     car1 = f"{car["year"]} {car["company"]} {car["model"]}: "
#     while True:
#         user = input("\nYou: ")
#         if user.lower() in {"exit", "quit"}:
#             break
#         reply = await car_response(user, history, car1, personality)
#         print(car1, reply)
#         history.append({"user": user})
#         history.append({car1: reply})


# asyncio.run(ai(car, personality, history))
