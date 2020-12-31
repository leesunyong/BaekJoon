A, B, C = int(input()), int(input()), int(input())
num = list(str(A * B * C))
for i in range(10):
    print(num.count(str(i)))