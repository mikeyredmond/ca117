#!/usr/bin/env python3

import sys

def main():
   string = sys.argv[1]
   integer = int(sys.argv[2])
   l = []
   for letter in string:
      l.append(letter)
   i = 0
   while i < integer:
      tmp = l[0]
      l.pop(0)
      l.append(tmp)
      i += 1

   ns = "".join(l)
   print(ns)

if __name__ == '__main__':
   main()
