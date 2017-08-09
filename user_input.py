import random
import main
import synonym_parser

# loaded from file, key is the root word and value is a list of synonyms
dictionary = []
dictionary_filename = "mobythes.aur"

# Gets a synonym for the given word from the given dict
# input: word - the word you want a synonym for
# output: synonym for the word
def get_synonym(word):
    # if word is key, i.e. we have synonyms for the word
    word = word.lower()
    if word in dictionary:
        synonyms = dictionary[word]
        return random.choice(synonyms)
    else:
        return word

# Determines if word should be replaced by a synonym
# output: True if replaceable, False if not
def is_replaceable_word(word):
    nonreplaceable = ['a','an','the','is']
    if word in nonreplaceable:
        return False
    else:
        return True

# Replaces every word in the input list with its synonym, if one exists
# input: input_list - list of words to replace
# output: list of words with input replaced by synonyms
def replace_with_synonyms(input_list):
    global dictionary
    if not dictionary:
        dictionary = synonym_parser.parse(dictionary_filename)
    output_list = []
    for i in range(len(input_list)):
        if is_replaceable_word(input_list[i]):
            output_list.append(get_synonym(input_list[i]))
        else:
            output_list.append(input_list[i])
    return output_list

# Prompts the user for a sentence and returns a list of words in the sentence
# output: list of words in the sentence            
def take_user_input():
    input_list = input("Enter a sentence to be paraphrased: ").split()
    return input_list