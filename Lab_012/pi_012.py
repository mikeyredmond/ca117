#!/usr/bin/env python3

import sys

from math import pi

def p(dec):
   m = str(dec)
   n = "{:." + m + "f}"
   return(n.format(pi))

def main():
   print(p(sys.argv[1]))

if __name__ == '__main__':
   main()
