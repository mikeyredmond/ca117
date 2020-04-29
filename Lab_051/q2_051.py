#!/usr/bin/env python3

import sys

def main():
   a = []
   for line in sys.stdin:
      s = line.lower().strip()
      l = [c for c in s if c in 'evil']
      if l == list('evil'):
         print(line.strip())

if __name__ == '__main__':
   main()
