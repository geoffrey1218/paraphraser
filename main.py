import user_input
import synonym_parser

def main():
    running = True
    while running:
        original_msg = user_input.take_user_input()
        new_msg = user_input.replace_with_synonyms(original_msg)
        print(new_msg)
        again = input("Another? ").lower()
        running = again == 'y' or again == "yes" or again == "si"

if __name__ == "__main__":
    main()
