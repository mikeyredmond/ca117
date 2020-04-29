#!/usr/bin/env python

import sys
'''Capitalising first and last character'''

def capital(s):
   if len(s) > 1:
      if len(s) > 2:
         return s[0].capitalize() + s[1:-1] + s[-1].capitalize()
      else:
         return s[0].capitalize() + s[-1].capitalize()

def main():
   for line in sys.stdin:
      final = capital(line.strip())
      if final:
         print(final)

if __name__ == '__main__':
   main()
