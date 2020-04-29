#!/usr/bin/env python3

import sys

def sorter(s):
   return s[1]

def dictionary(s):
   d = {}
   with open(s, "r") as f:
      for line in f:
         l = line.strip().split()
         d[" ".join(l[:-1])] = int(l[-1])
      return d

def main():
   d1 = {}
   a = dictionary(sys.argv[1])
   for lines in sys.stdin:
      total = 0
      l = lines.strip().split(",")
      i = 1
      while i < len(l):
         if l[i] in a:
            total += a[l[i]]
         else:
            total += 100
         i += 1
      d1[l[0]] = total

   for k, v in sorted(d1.items(), key=sorter):
      maxkwidth = len(max(d1.keys(), key=len))
      maxvwidth = len(str(max(d1.values())))
      print('{:>{}s} : {:{}d}'.format(k, maxkwidth, v, maxvwidth))

if __name__ == '__main__':
   main()
