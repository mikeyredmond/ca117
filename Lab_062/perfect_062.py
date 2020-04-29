#!/usr/bin/env python3

import sys

def sumFac(n):
   count = 0
   for i in range(1, (n // 2) + 1):
      if n % i == 0:
         count = count + i
   return count

def isPerfect(n):
   if n == sumFac(n):
      print(True)
   else:
      print(False)

def main():
   for line in sys.stdin:
      n = int(line.strip())
      isPerfect(n)

if __name__ == '__main__':
   main()
