command = ""
car_started = False
car_stopped = False

while True:
    command = input("> ").lower()
    if command == "start":
        if car_started != True:
            print("Car started...Ready to go:")
            car_started = True
        else:
            print("Hey, the car is already started, what are you doing?")
    elif command == "stop":
        if car_stopped != True:
            print("Car stopped.")
            car_stopped = True
        else:
            print("Hey, the car is already stopped, what are you doing?")
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
