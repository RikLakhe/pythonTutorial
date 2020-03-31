temperatures = [10, -20, -289, 100]


def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9 / 5 + 32
        return f

with open('temp.txt', 'w') as file:
    for t in temperatures:
        try:
            test = float(c_to_f(t))
            file.write(str(test)+'\n')
        except:
            print('not added')
