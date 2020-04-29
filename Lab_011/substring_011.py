#!/usr/bin/env python

'''Program should print True if substring of 2nd string.'''

import sys

def string(s):
   t = s.split()
   return t[0] in (t[1])

def main():
   for line in sys.stdin:
      sub = string(line.lower().strip())
      print(sub)

if __name__ == '__main__':
   main()
