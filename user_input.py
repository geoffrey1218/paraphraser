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
def replace_with_synonyms(input_list):
    for i in range(len(input_list)):
        if is_replaceable_word(input_list[i]):
            input_list[i] = input_list[i].upper()

# Prompts the user for a sentence and returns a list of words in the sentence
# output: list of words in the sentence            
def take_user_input():
    input_list = input("Enter a sentence to be paraphrased: ").split()
    return input_list