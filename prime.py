"""
prime.py -- Write the application code here
"""


def generate_prime_factors(value):
    int(value)
    list1 = []
    num = 2
    while value >= 2:
        if value % num == 0:
            list1.append(num)
            value = value / num
        else:
            num = num + 1
    return list1
