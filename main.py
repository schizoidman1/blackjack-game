from replit import clear
import random
from art import logo


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  return random.choice(cards)

def calculate_score(cards):
  score = sum(cards)
  if len(cards) == 2 and score == 21:
    return 0
  if 11 in cards and score > 21:
    cards.remove(11)
    cards.append(1)
  return score

def compare(user_score, computer_score):
  if user_score == computer_score:
    print("It's a draw")
    print(computer_score)
  elif computer_score == 0:
    print("You Lose...")
    print(computer_score)
  elif user_score == 0:
    print("You Won!")
    print(computer_score)
  elif user_score > 21:
    print("You Lose...")
    print(computer_score)
  elif computer_score > 21:
    print("You Won!")
    print(computer_score)
  else:
    if user_score > computer_score:
      print("You Won!")
      print(computer_score)
    elif computer_score > user_score:
      print("You Lose...")
      print(computer_score)

def blackjack():
  user_cards = []
  computer_cards = []

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  is_running = True
  while is_running:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards:{user_cards}     current score:{user_score}")
    print(f"Computer cards:[{computer_cards[0]}, ***]")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_running = False
    else:
      if input("Do you want to draw another card? 'y' or 'n'\n") == "y":
        user_cards.append(deal_card())
        clear()
      else:
        is_running = False

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  compare(user_score, computer_score)
print(logo)
def start_game():
  clear()
  print(logo)
  if input("Welcome to the Blackjack Capstone Game!\nType 'y' to play:\n") == 'y':
    clear()
    blackjack()
    restart_game()
  else:
    clear()
    print(logo)
def restart_game():
  if input("Do you want to restart the game? 'y' or 'n':\n") == 'y':
    start_game()
  else:
    clear()
    print(logo)
start_game()
