#!/usr/bin/env python3

import sys

def main():
   vowels = 'aeiou'
   for line in sys.stdin:
      a = line.strip()
      a = a.split(maxsplit=0)
      b = []
      for word in a:
         for char in word:
            b.append(char)
      i = 0
      while i < len(b):
         if b[i] in vowels:
            b.pop(i + 1)
            b.pop(i + 1)
         i += 1
      print(''.join(b))

if __name__ == '__main__':
   main()
