#!/usr/bin/env python3

import sys

def cap(s):
   i = 0
   while i < len(s):
      s[i] = s[i].capitalize()
      i += 1
   return " ".join(s)

def main():
   for line in sys.stdin:
      word = line.lower().strip().split()
      new = cap(word)
      print(new)

if __name__ == '__main__':
   main()
