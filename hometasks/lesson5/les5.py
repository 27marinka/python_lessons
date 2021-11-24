def my_sum(iter_obj, start = 0):
    """
    function of sum of the objects
    """
    for itm in iter_obj:
        start += itm
    return start

def enumerate_my(iter_obj, start = 0):
    result = zip(range(start, start + len(iter_obj)), iter_obj)
    return tuple(result)

a = enumerate_my([1, 2, 3], 10)
                 
print(a)

