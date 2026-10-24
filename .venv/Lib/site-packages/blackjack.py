import random

suits = ['♠', '♥', '♦', '♣']
ranks = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
cards = []
face_cards = ['J', 'Q', 'K']

for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])

random.shuffle(cards) 

deal = random.sample(cards, k=4)
player_hand = deal[0:2]
dealer_hand = deal[2:4]

def count_score(hand, owner_label):
    owner_score = 0
    owner_formatted_string = f'{owner_label} cards: '
    for card in hand:
        suit, rank = card
        if rank in range(2, 11):
            owner_score += rank
        elif rank in face_cards:
            owner_score += 10
        elif rank == 'A':
            if owner_score <= 10:
                owner_score += 11
            else:
                owner_score += 1
        owner_formatted_string += f'{suit} {rank}, ' 
    owner_formatted_string += f'total score: {owner_score}'

    return  [owner_score, owner_formatted_string]

player_formatted_string = count_score(player_hand, 'Player')
dealer_formatted_string = count_score(dealer_hand, 'Dealer')

player_score = player_formatted_string[0]
dealer_score = dealer_formatted_string[0]

print(player_formatted_string[1])
print(dealer_formatted_string[1])

if player_score > dealer_score:
    print('YOU WIN!')
elif dealer_score > player_score:
    print('YOU LOSE!')
elif dealer_score == player_score:
    print('TIE!')









