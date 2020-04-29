#!/usr/bin/env python3

import sys

vowels = ["a", "e", "i", "o", "u"]
def main():
   for line in sys.stdin:
      l = []
      for char in line.lower():
         if char in vowels:
            l.append(char)
      if l == vowels:
         print(line.strip())

if __name__ == '__main__':
   main()
