def recur_factorial(n):
    return 1 if n==1 else n*recur_factorial(n-1)

recur_factorial(4)  # 4! = 4 x 3 x 2 x 1 = 24
