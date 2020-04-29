#!/usr/bin/env python3

import sys

def main():
   s = list(sys.argv[1])
   i = 1
   while i < len(s):
      s[i], s[i - 1] = s[i - 1], s[i]
      i += 2
   print("".join(s))

if __name__ == '__main__':
   main()
