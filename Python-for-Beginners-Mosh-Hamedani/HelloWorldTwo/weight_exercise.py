user_weight = input('Weight: ')
weight_type = input('(L)bs or (K)g: ')
if weight_type.upper() == "L":
    weight_in_kg = float(user_weight) * 0.45
    formatted_float = "{:.1f}".format(weight_in_kg)
    print('You are ' + formatted_float + ' kilos')
elif weight_type.upper() == 'K':
    weight_in_lbs = float(user_weight) / 0.45
    formatted_float = "{:.1f}".format(weight_in_lbs)
    print('You are ' + formatted_float + ' pounds')

# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")