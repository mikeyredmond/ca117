#!/usr/bin/env python

import sys

def cap(s):
   i = 0
   while i < len(s):
      s[i] = s[i][:len(s[i]) - 1] + s[i][len(s[i]) - 1].capitalize()
      i += 1
   return " ".join(s)

def main():
   for line in sys.stdin:
      word = line.lower().strip().split()
      print(cap(word))

if __name__ == '__main__':
   main()
