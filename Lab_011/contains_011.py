#!/usr/bin/env python

import sys

def contain(char, s):
   for c in char:
      if c in s:
         s = s.replace(c, "", 1)
      else:
         return False
   return True

def main():
   for line in sys.stdin:
      [char, s] = line.lower().strip().split()
      print(contain(char, s))

if __name__ == '__main__':
   main()
