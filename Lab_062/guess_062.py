def find():
    t = top
    b = bottom
    while b < t:
        mid = (b + t) // 2
        g = guess(mid)
        if g == 0:
            return mid
        elif g == -1:
            b = mid + 1
        elif g == 1:
            t = mid
    return b
