
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
