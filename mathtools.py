#!/usr/bin/env python
from math import factorial

class mathtools:
    def __init__(self):
        pass

    @staticmethod
    def is_prime(x: int) -> bool:
        if not isinstance(x, int):
            return None

        elif x < 0:
            return None

        elif x == 0 or x == 1:
            return False

        elif x == 2:
            return True

        else:
            for n in range(2, x):
                if x % n == 0:
                    return False

        return True

    @staticmethod
    def combination(a: int, b: int) -> int:
        return int( factorial(a) / (factorial(b) * factorial(a - b)) )

    @staticmethod
    def permutation(a: int, b: int) -> int:
        return int( factorial(a) / factorial(a - b) )

    @staticmethod
    def get_divisors(x: int) -> list[int]:
        if not isinstance(x, int):
            return None

        if x == 0:
            return [float('inf'), float('-inf')]

        if x == 1:
            return [1, -1]

        if mathtools.is_prime(x):
            return [-abs(x), -1, 1, abs(x)]

        pos_divisors: list[int] = []

        for i in range(1, x+1):
            if x % i == 0:
                pos_divisors.append(i)

        neg_divisors: list[int] = []

        for divisor in pos_divisors:
            neg_divisors.append(-divisor)

        neg_divisors = neg_divisors[::-1]
        all_divisors = neg_divisors + pos_divisors

        return all_divisors

    @staticmethod
    def get_pos_divisors(x: int) -> list[int]:
        return list( set ([abs(i) for i in mathtools.get_divisors(x)] ))

    @staticmethod
    def get_neg_divisors(x: int) -> list[int]:
        return sorted(list( set ([-abs(i) for i in mathtools.get_divisors(x)])))

    @staticmethod
    def remove_same_values(x: list[int]) -> list[int]: return list(set(x))

if __name__ == "__main__":
    # for unit testing i use directly calling python script!
    import os

    remove_tab = '\b'*4
    rt = remove_tab

    while True:
        try:
            os.system('cls')
            print('\n' + str(mathtools.get_divisors(int(input("Bölenlerin sayısını bulmak için sayı girin: ")))))
            n, r = list(map(int, input("\nGive me two numbers for calculate permutation and combination: ").split()))
            break
        except ValueError:
            pass

    print(f"""
    {rt}(n, r) = ({n}, {r})
    {rt}Combination: {mathtools.combination(n, r)}    | C({n}, {r}) = {mathtools.combination(n, r)}
    {rt}Permutation: {mathtools.permutation(n, r)}    | P({n}, {r}) = {mathtools.permutation(n, r)}
    {rt}"""
    )

    print("Positive and negative dividors: ")
    print("Positive dividors:", mathtools.get_pos_divisors(12))
    print("Negative dividors:", mathtools.get_neg_divisors(12))
