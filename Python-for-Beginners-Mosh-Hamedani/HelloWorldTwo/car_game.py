user_input = input(">").upper()

i = 1
if user_input == "HELP":
    print("""
        start - to start the car
        stop - to stop the car
        quit - to exit""")
    while i == 1:
        selected_command = input(">").upper()
        if selected_command == "START":
            print("Car started...Ready to go:")
        elif selected_command == "STOP":
            print("Car stopped.")
        elif selected_command == "QUIT":
            break