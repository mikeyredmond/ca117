#!/usr/bin/env python3

import sys

def main():
   fl = sys.stdin.readline().strip().split()
   sl = sys.stdin.readline().strip().split()
   final_list = []
   for num in sl:
      fl.append(num)

   i = 0
   while i < len(sl):
      if fl[i] == fl[i + len(sl)]:
         final_list.append(i)
      i += 1
   print(final_list)

if __name__ == '__main__':
   main()
