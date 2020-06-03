#!/usr/bin/python3
import random
random.seed(1)

def generate_seq(k,length):
    return [tuple(sorted(random.sample(range(k),2))+[random.randint(1,100)]) for _ in range(length)]
