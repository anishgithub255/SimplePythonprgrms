import random

top_of_range = input("type any number ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("enter a larger number ")
        quit()
else:
      print("enter a number ") 
      quit()


random_number = random.randint(0,top_of_range)
guesses=0

while True:
      guesses += 1
      user_guess = input("Make a guess: ")
      if user_guess.isdigit():
          user_guess = int (user_guess)
      else:
          print("enter a number ")
          continue

      if user_guess == random_number:
          print("You got it right!")   
          break 
      elif user_guess < random_number:
            print("your number is greater than the random number!") 
      else:
            print("your number is lesser than the random number!")  

print("You got it", guesses , "guesses")             
