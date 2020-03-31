import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find_meanings(word):
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s ? Enter 'Y' for yes and 'N' for no :" % get_close_matches(word, data.keys())[0]).upper()
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return ['Please try again.']
        else:
            return ['Invalid entry.']
    else:
        return ['Word does not exist']


input_word = input('Enter word:').lower()

for meaning in find_meanings(input_word):
    print(meaning)