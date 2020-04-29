#!/usr/bin/env python3

import sys

def main():
   try:
      with open(sys.argv[1]) as f:
         bm = -1
         for line in f:
            mark, name = line.strip().split(" ", 1)
            if bm < int(mark):
               bm, bs, = int(mark), name
            elif int(mark) == bm:
               bs + ", " + name
      print("Best student:", bs)
      print("Best mark:", bm)
   except FileNotFoundError:
      print("The file", sys.argv[1], "could not be opened.")
   except ValueError:
      print("Invalid mark", mark, "encountered.", "Exiting.")

if __name__ == '__main__':
   main()
