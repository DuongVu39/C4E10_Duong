
def sum_to(n):
    """Return the sum of all interger number up to and including n"""
    S = 0
    for i in range (n+1):
        S += i
    print(S)


sum_to(4)
