def celcius_to_fahrenheit(celcius):
    return celcius * (9 / 5) + 32


input_number = input('Enter temperature in celcius:')

try:
    input_float_number = float(input_number)
    if input_float_number < -273.15:
        print('Temperature cannot be less than -273.15C')
    else:
        print('Temperature in Fahrenheit:', celcius_to_fahrenheit(input_float_number),"F")

except:
    print('Please enter number.')
