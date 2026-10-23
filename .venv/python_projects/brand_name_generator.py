import time
import random

sample = ['Bank', 'Hedge', 'Hustle', 'Origin', 'Bustling', 'Money']

print("Starting...")
time.sleep(2)
print("Welcome to Brandify, generate random brand names!")
time.sleep(2)
answer = input("Type a word: ").capitalize()

random_number = random.randint(0, len(sample) - 1)
answer += sample[random_number].capitalize()

print(f'Your brand name is: "{answer}"')