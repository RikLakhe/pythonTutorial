def celsiustofahrenheit (celcius):
    fahrenheit = float(float(celcius) * (9 / 5) + 32)
    return fahrenheit


inputCelcius = input('Enter Celcius : ')

print('Temperature in Fahrenheit:', celsiustofahrenheit(inputCelcius))
