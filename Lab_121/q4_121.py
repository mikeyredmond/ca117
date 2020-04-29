#!/usr/bin/env python3

import sys

def main():
   for line in sys.stdin:
      line = line.strip()
      nl = []
      nl.append(line[0])
      i = 1
      while i < len(line):
         if line[i].isupper():
            nl.append(" ")
            nl.append(line[i])
         else:
            nl.append(line[i])
         i += 1
      nw = "".join(nl)
      print(nw.capitalize())

if __name__ == '__main__':
   main()
