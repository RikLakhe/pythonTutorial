def input_string_length(word):
    return len(word)


words = input('Length word: ')

try:
    float(words)
    print("Sorry integers don't have length")
except:
    print("Length is :", input_string_length(words))
