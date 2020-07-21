user_input = input("Phone: ")
numbers = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"

}
result_string = ""

for digit in user_input:
    result_string += numbers[int(digit)] + " "

print(result_string)