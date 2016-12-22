def is_replaceable_word(word):
    nonreplaceable = ['a','an','the','is']
    if word in nonreplaceable:
        return False
    else:
        return True

def replace_with_synonyms(input_list):
    for i in range(len(input_list)):
        if is_replaceable_word(input_list[i]):
            input_list[i] = input_list[i].upper()
    
def take_user_input():
    input_list = input("Enter a sentence to be paraphrased: ").split()
