"""
prime.py -- Write the application code here
"""


def generate_prime_factors(value):
    int(value)
    list1 = []
    list2 = [2, 3]
    while(value >= 2):
        for num in list2:
            if (value % num == 0):
                list1.append(num)
                value = value / num

    return list1
