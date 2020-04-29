#!/usr/bin/env python3

import sys

def contacts(d):
   for line in sys.stdin:
      f = line.strip()
      if f in d:
         print("Name:", f)
         print("Phone:", d[f])
      else:
         print("Name:", f)
         print("No such contact")


def main():
   d = {}
   with open(sys.argv[1], "r") as f:
      for line in f:
         f_line = line.strip().split()
         d[f_line[0]] = f_line[1]
      contacts(d)

if __name__ == '__main__':
   main()
