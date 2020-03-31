file = open('fruits.txt', 'r')

content = file.read()

print(content)

file.seek(0)

content = file.readlines()
content = [i.rstrip("\n") for i in content]

for line in content:
    print(line)



file.close()