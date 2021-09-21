# lucky unicorn base code
import random
# ****** Funcion goes here ******
def yes_no(question):
  valid = False
  while not valid:
            response = input("Have you played this game "
                         "before? ").lower()

            if response == "yes" or response == "y":
                response = "yes"
                return response

            elif response == "no" or response == "n":
                response = "no"
                return response

            else:
                print("Please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print("Enter amount you want to play with \n"
          "Press enter to play and see how long your money can last in the game")
    print()
    return ""


def num_check (question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / high give
            if 0 < response <= 10:
                return response


                # output an error
            else:
                print(error)

        except ValueError:
            print(error)


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement =  "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here
# Welcome message
statement_generator("Welcome to the lucky unicorn Game", "*")

# Ask user if they  have played before
played_before = yes_no("Have you played the game before? ")
# display instructions if not played before
if played_before == "no":
    instructions()
    print()

# ask user how much they want to play with
how_much = num_check("How much do you want to play with", 0, 10)
# displays to user how much they have chosen to play with
print(" you will be spending ${}".format(how_much))



#initiates variables
balance = how_much
rounds_played = 0

# set up loop to engage game and play multiple rounds
play_again = input("press <Enter> to play...").lower()
while play_again == "":
    # add to rounds played to count amount rounds played
    rounds_played +=1
    # displays
# increase # of rounds played
    rounds_played += 1

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        decoration = "!"
        balance += 4
    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    if 6 <= chosen_num <= 36:
        chosen = "donkey"
        decoration = "D"
        balance -= 1

    # The token is either a horse or a zebra...
    # in both instances, subtract $0.50 from the balance
    else:
        # if the is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            decoration = "L"
        # otherwise set it to a zebra
        else:
            chosen = "zebra"
        balance -= 0.5
        decoration = "0"
    feedback = "You got a {}. Your balance is ${:.2f}".format(chosen, balance)
    statement_generator(feedback,decoration)

    if balance < 1:
        # if balance is to low, exit the game and
        # output  a suitable message
        play_again = "xxx"
        print("sorry you have run out of money")

        play_again = input("Press Enter to play again")
