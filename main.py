import user_input
import parser

dictionary_filename = "mobythes.aur"

def init():
    dictionary = parser.parse(dictionary_filename)

def main():
    running = True
    while running:
        original_msg = user_input.take_user_input()
        new_msg = user_input.replace_with_synonyms(original_msg)
        print(new_msg + '\n')
        again = input("Another? ").lower()
        running = again == 'y' or again == "yes" or again == "si"

if __name__ == "__main__":
    main()
