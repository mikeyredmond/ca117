def count_letters(s):
   if len(s) == 0:
      return 0
   return len(s) + count_letters(s[len(s):])
