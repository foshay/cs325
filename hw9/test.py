from judge_hw9 import judge
def generate_seq(k,length,seed): import random; random.seed(seed); return [tuple(sorted(random.sample(range(k),2))+[random.randint(5,10)]) for _ in range(length)]
dense_tuples = generate_seq(1000, 50000, 1)
tuples_1 = generate_seq(5000, 50000, 1)
tuples_2 = generate_seq(5000, 50000, 4)

judge(1000, dense_tuples[:1000], 96)
judge(1000, dense_tuples[:5000], 25)
judge(1000, dense_tuples[:10000], 8)
judge(5000, tuples_1[:5000], 111)
judge(5000, tuples_1[:7500], 66)
judge(5000, tuples_1[:9000], 53)
judge(5000, tuples_1[:20000], 25)
judge(5000, tuples_2[:7000], 34)
judge(5000, tuples_2[:15000], 33)
judge(5000, tuples_2[:16000], 33)
