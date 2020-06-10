command = ""
# I was thinking a lot: how I can use the variable in the while condition if I declare it inside while condition
# how I can use the variable before its declaration
# the answer is simple: simply declare the variable, assign default value and use variable in while condition
# (then change value of variable inside while loop)
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started...Ready to go:")
    elif command == "stop":
        print("Car stopped.")
    # facepalm (- -) just because author typed help command first, I thought user will first type help, and separated this command from others.
    # But this is same command as start, stop
    elif command == "help":
        # when you use triple quotes, message appears as it is (with indentation)
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")



