import os
import random
import json

current_directory = os.path.dirname(__file__)
root_directory = os.path.abspath(os.path.join(current_directory, "..", ".."))


def generate_new_car():
    car_data = os.path.join(root_directory, "CAR_DATA.json")

    random_id = random.randint(0, 999)

    with open(car_data, "r") as file:
        car = json.load(file)[random_id]

    return car


def car_personality():
    personality_data = os.path.join(root_directory, "PERSONALITY_DATA.json")

    random_id = random.randint(0, 19)

    with open(personality_data, "r") as file:
        personality = json.load(file)[random_id]

    return personality
