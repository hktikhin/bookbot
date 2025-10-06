def get_num_words(contents):
  return len(contents.split())

def get_num_each_char(contents):
  counter = {}
  for char in contents:
    char = char.lower()
    if char not in counter.keys():
      counter[char] = 1
    else:
      counter[char] += 1
  return counter

def sort_num_each_char(counter):
  char_counts = [{"char": char, "num": num} for char, num in counter.items()]
  char_counts.sort(reverse=True, key=lambda item:item["num"])
  return char_counts
  
