from itertools import permutations


def ram_overload(num=1):
    num *= 50000000
    a = permutations([i for i in range(num)])