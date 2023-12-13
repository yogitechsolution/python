# input phone numbers will be translated into words

phone = input("Phone: ") # storing entered value in phone variable e.g 1234
#create a dictionary to translate the value of each character in to a word
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = "" #initially set with empty string
for ch in phone: #Get each value of a character
    output += digits_mapping.get(ch, "!") + " " #use .get so prog not yell & '!' for non-existing character & " " for space at the END
print(output)

#o/p
#Phone: 1234
#One Two Three Four 

#Phone: 1235
#One Two Three !

