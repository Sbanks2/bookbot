import re

def count_str(file_contents):
     split_text = file_contents.split()
     return len(split_text)

def char_count(file_contents):
     lower = file_contents.lower()
     c_count = {}
     for c in lower:
          if c not in c_count:
               c_count[c] = 1
          else:
               c_count[c] += 1
     return c_count


def main():
     with open("books/frankenstein.txt") as f:
          file_contents = f.read()
     count_str(file_contents)

     character_dict = char_count(file_contents)
     list_of_char_dict = [{key: value} for key, value in character_dict.items()]
     list_of_char_dict.sort(reverse = True, key = lambda d: list(d.values())[0])

     print("--- Begin report of books/frankenstein.txt ---")
     print(f"{count_str(file_contents)} words found in the document")
     print()

     for dict in list_of_char_dict:
          for key, value in dict.items():
               if key.isalpha():
                    print(f"The '{key}' character was found {value} times")
     print("--- End report ---")

if __name__ == "__main__":
     main()