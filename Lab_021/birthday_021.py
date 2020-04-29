#!/usr/bin/env python3

import sys
import calendar

def wday(y, m, d):
   w = calendar.weekday(y, m, d)
   if w == 0:
      return "You were born on a Monday and Monday's child is fair of face."
   elif w == 1:
      return "You were born on a Tuesday and Tuesday's child is full of grace."
   elif w == 2:
      return "You were born on a Wednesday and Wednesday's child is full of woe."
   elif w == 3:
      return "You were born on a Thursday and Thursday's child has far to go."
   elif w == 4:
      return "You were born on a Friday and Friday's child is loving and giving."
   elif w == 5:
      return "You were born on a Saturday and Saturday's child works hard for a living."
   elif w == 6:
      return "You were born on a Sunday and Sunday's child is fair and wise and good in every way."


def main():
   d = int(sys.argv[1])
   m = int(sys.argv[2])
   y = int(sys.argv[3])
   print(wday(y, m, d))


if __name__ == '__main__':
   main()
