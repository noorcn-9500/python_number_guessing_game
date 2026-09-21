# Number Guessing Game

def guessnum(number, attempt=1):
  your_guesses = []
  result_guesses = []
  try:
    attempts = input("Challenge the Number of Attempts: ")
    print("-----------------------------------\n")
    max_attempt = int(attempts)
  except ValueError:
    print("Please enter a valid attempt number\n")

  while (attempt <= max_attempt):
    running_attempt = attempt
    try:
      guessed = input(f"Attempt {attempt}/{max_attempt} - Enter your guess: ")
      guessed = int(guessed)  #Will raise Exception if not a valid number

      if guessed < 1 or guessed > 100:
        print("!!!Enter number between 1 and 100!!!\n")

      else:
        check_guess = lambda x,y: "Correct" if x == y else ("Less" if x < y else "High")
        result = check_guess(guessed,number)

        if result == "Correct":
          print("-------------------------")
          print("Congratulations. You won..!")
          your_guesses.append(guessed)
          print("Your Guesses are: ")
          for gst in your_guesses:
            result_guesses.append(gst)
          print(result_guesses)
          print(f"You Won in - {attempt} - attempts")
          print("-------------------------")
          return
    
        if result == "Less":
          if attempt == max_attempt:              #last attempt
            your_guesses.append(guessed)
            break
          else:
            print("Guess Higher Number\n")
            your_guesses.append(guessed)
            attempt+=1

        if result == "High":
          if attempt == max_attempt:             #last attempt
            your_guesses.append(guessed)
            break
          else:
            print("Guess Lower Number\n")
            your_guesses.append(guessed)
            attempt+=1
    except ValueError:
      print("Please enter a valid number.\n")
      attempt = running_attempt
    
    if attempt == 4 :
      if number % 2 == 0:
        print("Hint: It is an Even Number")
      else:
        print("Hint: It is an Odd Number")
  
  print("\nGame Over. Better luck Next Time..!")      
  print("Your Guesses are: ")
  for gsn in your_guesses:
    result_guesses.append(gsn)
  print(result_guesses)  
  print(f"\nThe Number is: {number}")
  
while True:
  random_number = random.randint(1,100)
  #print(random_number)
  print("!..Guess the Number..!")
  guessnum(random_number)
  play_again = input("\n--> Want to Play again (Y/N): ")
  if play_again == 'N':
    break
  