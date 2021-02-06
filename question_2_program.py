def averageList(target):
    if len(target) < 1:
        raise ValueError("List must have at least one element")

    for i in target:
        if (not isinstance(i,int)) and (not isinstance(i, float)):
            raise TypeError("Can only take the average of numbers")

    total = 0
    for i in target:
        total += i

    return total/len(target)