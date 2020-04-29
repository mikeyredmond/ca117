#!/usr/bin/env python3

import sys
import string

vowels = 'aeiou'

def sorter(t):
   return t[1]

def main():
   a = []
   for line in sys.stdin:
      s = line.lower().strip().strip(string.punctuation).split()
      for l in s:
         s = a.append(l.strip(string.punctuation))
   count = {}.fromkeys(vowels, 0)
   for key in a:
      for char in key:
         if char in count:
            count[char] += 1
   max_v_width = len(str(max(count.values())))
   for (k, v) in sorted(count.items(), key=sorter, reverse=True):
      print('{} : {:{}d}'.format(k, v, max_v_width))

if __name__ == '__main__':
   main()
