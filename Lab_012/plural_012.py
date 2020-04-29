#!/usr/bin/env python3

import sys

def plural(char):
   if char[-1] == "x" or char[-1] == "o" or char[-1] == "s" or char[-1] == "z" or char[-2:] == "ch" or char[-2:] == "sh":
      return char + "es"
   elif char[-1] == "f":
      return char[:-1] + "ves"
   elif char[-2:] == "fe":
      return char[:-2] + "ves"
   elif (char[-1] == "y") and char[-2] != "a" and char[-2] != "e" and char[-2] != "i" and char[-2] != "o" and char[-2] != "u":
      return char[:-1] + "ies"
   else:
      return char + "s"


def main():
   for line in sys.stdin:
      print(plural(line.strip()))

if __name__ == '__main__':
   main()
