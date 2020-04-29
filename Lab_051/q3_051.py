#!/usr/bin/env python3

import sys


def main():
   s = ""
   for line in sys.stdin:
      for char in line:
         if char.islower():
            s = s + "0"
         else:
            s = s + char
   s = s.strip().split()
   i = 0
   while i < len(s):
      ns = s[i].split('0')
      print(max(ns, key=len))
      i += 1

if __name__ == '__main__':
   main()
