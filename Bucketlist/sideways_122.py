#!/usr/bin/env python3

import sys

def main():
   a = []
   lines = sys.stdin.read().strip().split()
   line_count = len(lines)
   line_length = len(lines[0])
   i = 0
   while i < line_length:
      a.append("")
      i += 1
   f = 0
   while f < line_length:
      for line in lines:
         a[f] += line[f]
      f += 1
   a = sorted(a, key=str.casefold)
   final = 0
   while final < line_count:
      finished_string = ''
      for element in a:
         finished_string = finished_string + element[final]
      print(finished_string)
      final += 1

if __name__ == '__main__':
   main()
