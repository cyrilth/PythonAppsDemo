import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(key):
    key = key.lower()
    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()]
    elif len(get_close_matches(key, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(key, data.keys())[0]).lower()
        if yn == "y" or yn == "yes":
            return data[get_close_matches(key, data.keys())[0]]
        elif yn == "n" or yn == "no":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:    
    for item in output:
        print(item)
else:
    print(output)