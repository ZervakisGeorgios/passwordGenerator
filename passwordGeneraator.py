'''
This script can be used to generator random passwords
'''

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}*;/,._-$"

def passGenerator(num):
    all = lower + upper + numbers + symbols
    password = "".join(random.sample(all, num))
    print(password)
    
num = input('Give the length of the password')
passGenerator(num)


