import random
import time


def quick_sort(lis_t):
    if len(lis_t) <= 1:
        return lis_t
    else:
        bace = lis_t[0]
        lover = [i for i in lis_t[1:] if i <= bace]
        higher = [i for i in lis_t[1:] if i > bace]
        return quick_sort(lover) + [bace] + quick_sort(higher)


def main(list_t):
    start = time.time()
    print(quick_sort(lis_t))
    end = time.time() - start

    return end


lis_t = [i for i in range(random.randint(1, 100000))]
random.shuffle(lis_t)
print(lis_t)
print(main(lis_t))
