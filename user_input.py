import random

# Gets a synonym for the given word from the given dict
# input: word - the word you want a synonym for
#        synonym_dict - dict where key is the root word and value is a list of synonyms
# output: synonym for the word
def get_synonym(word, synonym_dict):
    # if word is key, i.e. we have synonyms for the word
    if word in main.dictionary:
        synonyms = synonym_dict[word]
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
#        synonym_dict - dict where key is the root word and value is a list of synonyms
def replace_with_synonyms(input_list, synonym_dict):
    for i in range(len(input_list)):
        if is_replaceable_word(input_list[i]):
            input_list[i] = get_synonym(input_list[i], synonym_dict)

# Prompts the user for a sentence and returns a list of words in the sentence
# output: list of words in the sentence            
def take_user_input():
    input_list = input("Enter a sentence to be paraphrased: ").split()
    return input_list