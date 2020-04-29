#!/usr/bin/env python3

import sys

def build_dictionary(filename):
   d = {}
   with open(filename, "r") as f:
      for line in f:
         l = line.strip().split()
         d[l[0]] = int(l[1])
      return d

def extract_range(d, low, high):
   d1 = {}
   for key in d:
      if low <= d[key] <= high:
         d1[key] = d[key]
   return d1

if __name__ == '__main__':
   main()
