def minimum(l):
   if len(l) == 1:
      return l[0]
   n = minimum(l[:-1])
   if l[-1] < n:
      return l[-1]
   else:
      return n
