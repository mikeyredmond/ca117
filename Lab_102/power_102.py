def power(n, o):
   if o == 0:
      return 1
   return n * power(n, o - 1)
