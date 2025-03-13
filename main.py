import sys
from stats import get_num_words, get_num_characters, get_sorted_characters



def main():
    #f = get_num_words("books/frankenstein.txt")
    #print(f"{f} words found in the document")
    #file = ""
    #with open("books/frankenstein.txt") as f:
    #    file = f.read()
    
    #print(num_characters)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    num_characters = get_num_characters(file_contents)

    sorted_characters = get_sorted_characters(num_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words('books/frankenstein.txt')} total words")
    print("--------- Character Count -------")
    for char in sorted_characters:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['count']}")
    print("============= END ===============") 




main()
