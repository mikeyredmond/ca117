#!/usr/bin/env python3

import sys


d = {
   "0": "zero",
   "1": "one",
   "2": "two",
   "3": "three",
   "4": "four",
   "5": "five",
   "6": "six",
   "7": "seven",
   "8": "eight",
   "9": "nine",
   "10": "ten",
}

def main():
   for line in sys.stdin:
      a = ""
      s = line.strip().split()
      for n in s:
         a = a + d[n] + " "
      print(a[:-1])

if __name__ == '__main__':
   main()
