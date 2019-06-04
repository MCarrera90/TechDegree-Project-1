import random

high_score = []

def greeting():
    text = "Welcome the number guessing game!"
    number_of_characters = len(text)
    header = (number_of_characters * "-")
    footer = (number_of_characters * "-")
    print(header, "\n",text,"\n", footer)
    

def start_game():
    attempt_count = 1
    number = random.randint(1, 10)
    
    
    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: "))
        except ValueError as err:
            print("Oh no that's not a valid entry. Please try again")
        else:
            if guess == number:
                play_again = input("Great job! you guessed correctly, it took {} tries.\nWould you like to play again? Y/N:  ".format(attempt_count))
                high_score.append(attempt_count)
                if play_again.lower() == "y":
                    print ("\nThe current high score is {}.".format(min(high_score)))
                    start_game()
                else:
                    print("\nThanks for playing, the game is now over")
                break
            if guess > number:
                print("It's lower")
            attempt_count += 1   
            if guess < number:
                print("It's higher")
            continue

if __name__ == '__main__':
    greeting()
    start_game()
    
