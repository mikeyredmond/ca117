#!/usr/bin/env python3

import sys

def convert(s):
   a = []
   for c in s:
      if c.isalnum():
         a.append(c)
   return a == a[::-1]

def main():
   for line in sys.stdin:
      print(convert(line.lower()))

if __name__ == '__main__':
   main()
