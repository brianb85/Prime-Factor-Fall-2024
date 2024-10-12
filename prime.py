"""
prime.py -- Write the application code here
"""


def generate_prime_factors(value):
    int(value)
    list1 = []
    while(value >= 2):
        if (value % 2 == 0):
            list1.append(2)
            value = value / 2
        elif (value % 3 == 0):
            list1.append(3)
            value = value / 3




    return list1

