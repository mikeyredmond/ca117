#!/usr/bin/env python3

import sys

a = []
def conv(s):
   m = []
   for c in s:
      if c[-1].isalnum():
         m.append(c)
      else:
         m.append(c[:-1])
   for b in m:
      if b not in a:
         a.append(b)
   return len(a)


def main():
   tot = 0
   for line in sys.stdin:
      conv(line.lower().strip().split())

   print(len(a) - 1)


if __name__ == '__main__':
   main()
