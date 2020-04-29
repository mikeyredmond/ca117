#!/usr/bin/env python3

import sys

s = []
def main():
   i = 0
   for line in sys.stdin:
      s.append(line.strip())
   while not s[i].isdigit():
      print(s[i], "is not a number")
      i += 1
   print("Thank you for", s[i])

if __name__ == '__main__':
   main()
