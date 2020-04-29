#!/usr/bin/env python3

import sys
import string

def main():
   d = {}
   for line in sys.stdin:
      a = []
      line = line.strip().split()
      for word in line:
         testword = word.strip(string.punctuation).casefold()
         if testword not in d:
            d[testword] = 1
            a.append(word)
         elif testword in d:
            a.append('.')
      print(' '.join(a))

if __name__ == '__main__':
   main()
