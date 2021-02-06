def name(first, last):
    if not isinstance(first, str) and not isinstance(last,str):
        raise TypeError("Inputs must be strings")
    
    str(first).strip()
    str(last).strip()

    return first + " " + last