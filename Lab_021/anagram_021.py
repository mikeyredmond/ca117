#!/usr/bin/env python3

import sys

def co(ch, s):
   if len(ch) == len(s):
      for c in ch:
         if c in s:
            s = s.replace(c, "", 1)
         else:
            return False
      return True
   return False

def main():
   for line in sys.stdin:
      [ch, s] = line.lower().strip().split()
      print(co(ch, s))


if __name__ == '__main__':
   main()
