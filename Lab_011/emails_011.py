#!/usr/bin/env python3

import sys

def name(s):
   t = s.find("."[:])
   f = s[:t]
   c = f.capitalize() + " "
   i = 0
   while i < len(s) and (s[i] < "0" or "9" < s[i]):
      i = i + 1

   if i < len(s):
      g = s[t + 1:i]
      d = g.capitalize()

   return c + d

def main():
   for line in sys.stdin:
      new = name(line.strip())
      print(new)

if __name__ == '__main__':
   main()
