import sys
from stats import report
from stats import get_num_words

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many arguments.")
        sys.exit(1)
    else:
        get_input = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {get_input}")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(f"{get_input}")} total words")
        print("--------- Character Count -------")
        for i in report(f"{get_input}"):
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")
main()