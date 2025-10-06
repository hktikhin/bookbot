import sys
from stats import get_num_words, get_num_each_char, sort_num_each_char

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  filepath = sys.argv[1]
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  file_contents = get_book_text(f"{filepath}")
  print("----------- Word Count ----------")
  print(f"Found {get_num_words(file_contents)} total words")
  print("--------- Character Count -------")
  counter = get_num_each_char(file_contents)
  for item in sort_num_each_char(counter):
    if item["char"].isalpha():
      print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
  main()
