def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def count_words(contents):
  return len(contents.split())


def main():
  file_contents = get_book_text("books/frankenstein.txt")
  print(f"Found {count_words(file_contents)} total words")

if __name__ == "__main__":
  main()
