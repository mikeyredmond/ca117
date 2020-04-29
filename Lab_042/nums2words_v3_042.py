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

d1 = {}
def main():
   d1 = {}
   with open(sys.argv[1]) as f:
      for line in f:
         e, i = line.strip().split()
         d1[e] = i
   for line in sys.stdin:
         a = ""
         m = line.strip().split()
         for n in m:
            a = a + d1[d[n]] + " "
         print(a[:-1])


if __name__ == '__main__':
   main()
