import random

def playerPlays():
  return input("Choose between rock, paper,and scissors:")

def computerPlays():
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

def getGameResult(player_choice, computer_choice):
  rules = {
    "rock": {"rock": "It's a draw", "paper": "You lose", "scissors": "You win"},
    "paper": {"rock": "You win", "paper": "It's a draw", "scissors": "You lose"},
    "scissors": {"rock": "You lose", "paper": "You win", "scissors": "It's a draw"}
  }  
  return rules[player_choice][computer_choice]

while True:
  player_choice = playerPlays()
  computer_choice = computerPlays()
  print(f"Computer plays: {computer_choice}")


  game_play = getGameResult(player_choice,computer_choice)
  print(game_play)


  if "lose" in game_play:
    print(f"You lose this game.Thanks for playing! ")
    break