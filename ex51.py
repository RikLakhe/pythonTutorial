temperatures=[10,-20,-289,100]

def celcius_to_fahrenheit(celcius):
    try:
        celcius_string = float(celcius)
        if celcius_string < -239.15:
            print('Temperature cannot be less than -239.15')
        else:
            print('Temperature is',celcius_string*(9/5)+32,'F')
    except:
        print('Temperature is not number')


for temp in temperatures:
    celcius_to_fahrenheit(temp)