def cube(h,l,w):
    if (h <= 0) or (w <= 0) or (l <= 0):
        raise ValueError("Must use positive numbers")

    if not (isinstance(h, int) or
        isinstance(l, int) or
        isinstance(w, int)):
        raise TypeError("Must be of int type")

    return h*l*w
    

