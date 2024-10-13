"""
prime.py -- Write the application code here
"""


def generate_prime_factors(value):
    int(value)
    list1 = []
    list2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    while(value >= 2):
        for num in list2:
            if (value % num == 0):
                list1.append(num)
                value = value / num

    return list1
