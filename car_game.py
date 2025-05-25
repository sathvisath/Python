# This is a car game that will use while loop to run. It is an example of while loop including if-else, boolean. Gives a better understanding of loops involving other concepts

command = " "    # we will declare the variable here to store user input in while loop
started = False   
stopped = False
helped = False
while command != "quit":
    command = input("> Please give a command: ").lower()
    if command == "start":
        if started:           # if the user gives start command once the car will start and second time it will tell the user that car is laready started
            print("The car is already started")
        else:
            started = True
            print("The car is started..let's goooo..")
    elif command == "stop":   
        if stopped==False:    # we can also write it in this way , both ways work the same.
            stopped = True
            print("The car is stopped successfully")
        else:
            print("The car is already stopped")
    elif command == "quit":
        break
    elif command == "help":
        if helped:           # same for help
            print("I've told you to select a command")
        else:
            helped = True
            print("Select a command: start, stop, quit")
    else:
        print("Give a valid command")
