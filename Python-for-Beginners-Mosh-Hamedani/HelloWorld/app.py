weight_in_pounds = input('Type your weight (lbs): ')
weight_in_kg = float(weight_in_pounds) / 2.2046
formatted_float = "{:.2f}".format(weight_in_kg)
print ('Your weight in kg: ' + formatted_float)

# weight_in_kg = int(weight_in_pounds) * 0.45