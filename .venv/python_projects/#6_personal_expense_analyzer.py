expenses = [
    {"category": "food", "amount": 25},
    {"category": "transport", "amount": 10},
    {"category": "food", "amount": 40},
    {"category": "entertainment", "amount": 60},
    {"category": "transport", "amount": 15},
    {"category": "food", "amount": 30},
]

expense_amounts = [expense["amount"] for expense in expenses]

def is_big_expense(expense):

    return expense > 20

def gel_to_usd(expense):

    return round((expense * 0.39), 2)


big_expenses = list(filter(is_big_expense, expense_amounts))
expenses_usd = list(map(gel_to_usd, expense_amounts))
total_spending_gel = sum(expense_amounts)

def food_spending_total(expenses):
    return sum([expense["amount"] for expense in expenses if expense["category"] == "food"])

food_total = food_spending_total(expenses)

def is_food(expense):
    return expense["category"] == "food"

def food_expense_map(expense):
    return expense['amount']

def food_spending_total_2(expenses):

    food_expenses = list(filter(is_food, expenses))
    expenses = map(food_expense_map, food_expenses)
    
    return sum(expenses)

