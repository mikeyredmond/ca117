def maximum(l):
   if len(l) == 1:
      return l[0]
   n = maximum(l[:-1])
   if l[-1] > n:
      return l[-1]
   else:
      return n
