import sys
import art
import time
from functions import clear
from random import randint


# Variables for coloured text
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m"
black = "\033[0;30m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"


game_on = True

# Boss stats
boss_health = 100

# Player stats
player_health = 100
player_attack = 20

crit_chance = randint(1, 15)
crit_strenght = randint(1, 10)
crit_multiplier = player_attack / crit_chance + 5

loading = ["Loading. /", "Loading.. |", "Loading... \\", "Loading. |","Loading.. /", "Loading... |"] # You can make this into ascii art as well! (You can put it into the art.py file
# and call the variables in the array/list here)
boss_fight_anim = [ " ", "|         |", "||       ||", "|||     |||", "||||   ||||", "||||| |||||", "|||||||||||", "|||||F|||||", "|||| Fi||||", "|||s Fig|||", "||ss Figh||", "|oss Fight|", "Boss Fight"]
# Makes an animation by printing different strings.

print(Red + art.logo)
print(Blue + art.options)
player_input = input("> ").lower()



def game():
  for i in range(len(boss_fight_anim)):
    print(boss_fight_anim[i])
    time.sleep(0.4)
    clear()

  while True:

    if boss_health <= 0:
      print("You won!")
      break # Call the function for chapter 2 if you have one.
    
    elif player_health <= 0:
      print("You lost, try again!")
      #game() # Uncomment the game() to restart the game. Make sure to comment break to not create the possibility of bugs appereaing.
      break

    print("Boss Fight") # add in your own name here 
    print(art.fight_options)
    player_input = input("> ").lower()

    if player_input == "1" or player_input == "attack":
      if crit_chance > 5 or crit_chance < 15:
        player_attack *= crit_strenght

      boss_health -= player_attack

      print(f"You have delt {player_attack}\n")
      print(f"The bosses health is now {boss_health}")




if player_input == "1" or player_input == "start":

  for i in range(len(loading)): # Loops for the amount of itmes in the loading array/list.
    time.sleep(0.5) # waits half a second (Feel free to change this!)
    clear()
    print(loading[i])

    game()


elif player_input == "2" or player_input == "options":
  pass
  # Perhaps call another function

elif player_input == "3" or player_input == "credits":
  pass
  print(art.Credits)

elif player_input == "4" or player_input == "exit":
  sys.exit()

