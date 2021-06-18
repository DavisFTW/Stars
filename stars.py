def star(n : int ):
    for i in range(n):  # pirma iteracija = i=0
        print( " " * (n - i), "*" * (i * 2 + 1))   # 1, 3, 5... 
    for i in range(n, -2, -1):
        print(" " * (n - i), "*" * (i * 2 + 1))

star(6)
