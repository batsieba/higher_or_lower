from game_data import data 
from art import logo, vs
import random
from replit import clear

#print(logo)
def get_random_account():
  """Get random account from data"""
  return random.choice(data)


def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  #print(f'{name}: {account["follower_count"]}\n')
  return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  continue_game = True
  msg = ""
  account_b = get_random_account()
  
  while continue_game:
    account_a = account_b
    account_b = get_random_account()
    if account_a == account_b:
      account_b = get_random_account()
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    guess_result = check_answer(guess, account_a["follower_count"], account_b["follower_count"])
    if guess_result:
      score+=1
      msg = f'Good Job. Your score is {score}.'
    else:
      continue_game = False
      msg = f'Sorry, that was wrong. Final score: {score}'
    clear()
    print(logo)
    print(msg)

game()




