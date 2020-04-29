#!/usr/bin/env python

'''Print middle character of a string or "No middle character" if not'''

import sys

def middle(s):
   if len(s) % 2 != 0:
      return s[len(s) // 2]
   else:
      return "No middle character!"

def main():
   for line in sys.stdin:
      final = middle(line.strip())
      if final:
         print(final)

if __name__ == '__main__':
   main()
