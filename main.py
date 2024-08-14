#BlackJack Game using python
import random
import art

"""Returns a random card from deck"""


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


"""Take the cards and returns the score"""


def calculate_score(input_list):
    if sum(input_list) == 21 and len(input_list) == 2:
        return 0
    if 11 in input_list and sum(input_list) > 21:
        input_list.remove(11)
        input_list.append(1)
    return sum(input_list)


"""decision functions"""


def compare(uScore, cScore):
    if uScore == cScore:
        print("Game draw")
    elif cScore == 0:
        print(f"You lose , computer wins")
    elif uScore == 0:
        print(f"You win , computer loses")
    elif uScore > 21:
        print(f"You lose as you went over limit, computer wins")
    elif cScore > 21:
        print(f"You win as computer went over limit")
    elif uScore > cScore:
        print(f"You have higher score , You win")
    else:
        print(f"You lose as computer has higher score . Computer Wins ")


def play_game():
    print(art.logo)

    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    isGameOver = False
    """Add two cards to list"""
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    """for the user"""
    while not isGameOver:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards: {user_cards} Current Score : {user_score}")
        print(f"Computer's  First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isGameOver = True
        else:
            another_turn = input("Do you want to draw another card ? Type y for yes n for no").lower()
            if another_turn == 'y':
                user_cards.append(deal_card())
            else:
                isGameOver = True
    """For the computer"""
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your Final hand {user_cards} Your Score {user_score}")
    print(f"Your Computer hand {computer_cards} Your Score {computer_score}")
    compare(user_score, computer_score)

    while input("Do you want to restart the game Type 'y' for yes and 'n' for no").lower()=='y':
        print("\n" *20)
        play_game()

play_game()