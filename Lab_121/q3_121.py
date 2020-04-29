#!/usr/bin/env python3

import sys

def search(test_word):
   vowels = "aeiou"
   test_vowels = []
   for letter in test_word:
      if letter in vowels:
         test_vowels.append(letter)
   return test_vowels

def final(l):
   vowels = "aeiou"
   final_vowels = "".join(l)
   if final_vowels == vowels:
      return True

def main():
   for line in sys.stdin:
      word = line.strip()
      test_word = word.lower()
      nl = search(test_word)
      if final(nl) is True:
         print(word)

if __name__ == '__main__':
   main()
