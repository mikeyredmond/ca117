#!/usr/bin/env python3

import sys

def conv(n, m):
   i = 0
   s = 0
   while i < len(n):
      s += ((int(m) ** (len(n) - i - 1)) * int(n[i]))
      i += 1

   return s

def main():
   for line in sys.stdin:
      [n, m] = line.lower().strip().split()
      print(conv(n, m))

if __name__ == '__main__':
   main()
