import time

print('Welcome to tip calculator!')
time.sleep(2)

bill = int(input('What is your total bill? '))
user_count = int(input('How many of you? '))
tip_amount = int(input('What percentage would leave as a tip? '))

tip_actual = bill * (tip_amount / 100) / user_count
print("Processing...")
time.sleep(2)

print(f"Your tip is: ${tip_actual}")




    
