#TODO 1. Create a dictionary in this format:
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate():
    word = input("Enter a word: ").upper()
    try:
        output = [dictionary[letter] for letter in word]
    except KeyError:
        print("You didn't enter a name. Please try again.")
        generate()
    else:
        print(output)

generate()






