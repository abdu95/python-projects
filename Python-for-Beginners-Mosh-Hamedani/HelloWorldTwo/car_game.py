command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Hey, the car is already started, what are you doing?")
        else:
            started = True
            print("Car started...Ready to go:")
    elif command == "stop":
        # if the car is not started, it means it stopped
        if not started:
            print("Hey, the car is already stopped, what are you doing?")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")
