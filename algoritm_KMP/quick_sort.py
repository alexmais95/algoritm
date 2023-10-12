def choise_sort(lis_t):
    if len(lis_t) < 2:
        return lis_t
    else:
        base = lis_t[0]
        lover = [i for i in lis_t[1:] if i <= base]
        higher = [i for i in lis_t[1:] if i > base]
        return choise_sort(lover) + [base] + choise_sort(higher)


print(choise_sort([2, 5, 3, 7, 1, 1]))