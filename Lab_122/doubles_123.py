#!/usr/bin/env python3

import sys

def sorter(t):
   return(t[1])

def main():
   vowels = 'aeiou'
   d = {}
   for line in sys.stdin:
      line = line.strip()
      count = line.count('aa') + line.count('ee') + line.count('ii') + line.count('oo') + line.count('uu')
      d[line] = count

   a = []
   for k, v in sorted(d.items(), key=sorter, reverse=True):
      a.append(k)
   print(a[0])

if __name__ == '__main__':
   main()
