numb = 7

fibo0 = 1
fibo1 = 1

x = 0
while x < numb:
    fibo_num = fibo0 + fibo1
    fibo0 = fibo1
    fibo1 = fibo_num
    x += 1