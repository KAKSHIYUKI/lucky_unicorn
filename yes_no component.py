# main routine go's here
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


# Ask user if they  have played before
show_instructions = input("Have you played this game before?").lower()

# If yes, Output 'program continues'
if show_instructions.lower() == "yes":
    print("program continues")

elif show_instructions.lower() == "y":
    print("program continues")

# If no output 'Display instructions'
elif show_instructions.lower() == "no":
    print("Display Instructions")

elif show_instructions.lower() == "n":
    print("Display Instructions")

else:
    print("please enter yes / no")
