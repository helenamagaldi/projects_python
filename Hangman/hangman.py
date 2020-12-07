import random
import os 

words = ["helena", "raíra", "magaldi"]
secret_word = random.choice(words)

def start():
  number_letters = len(secret_word)
  dash = "-" * number_letters
  print(dash)
  lives = 10

  while lives > 0 and dash != secret_word:
    print(dash)
    print(lives)

    letter = input("Guess a letter from the secret word: ")

    os.system("clear")

    if len(letter) != 1:
      print("Just one letter please (:")
      dash = update_dash(secret_word, dash, letter)

    elif letter in secret_word:
      print("Way to go! You letter is present in the secret word")
      dash = update_dash(secret_word, dash, letter)

    else:
      print("Your letter is not here")
      lives -= 1

    if lives == 0:
      print("You lost ): The secret word was: " + secret_word)

    else:
      print("Congrats! You just won!")

def update_dash(secret_word, dash, letter):
  result = ""

  for i in range(len(secret_word)):
    if secret_word[i] == letter:
      result += letter

    else:
      result += dash[i]

  return result

start()
