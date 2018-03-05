import json

ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

alphabet_file = open("alphabet.json", "r")
alphabet_json = json.loads(alphabet_file.read())

missing_letters = []
for letter in ALPHABET:
    if letter not in alphabet_json:
        missing_letters.append(letter)

if len(missing_letters) > 0:
    print "WHAT HAVE YOU DONE?! WHERE ARE " + ', '.join(missing_letters)
    exit(2)
else:
    print "Good job, pal."
    exit(0)
