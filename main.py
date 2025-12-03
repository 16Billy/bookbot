from stats import count,count_char,report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

book_string = get_book_text(path)
num_words = count(book_string)
report_print = report(count_char(book_string))

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in report_print:
        print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")

main()