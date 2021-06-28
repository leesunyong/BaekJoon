num1 = int(input())
num2 = list(map(int, list(input())))

print(num1 * num2[2])
print(num1 * num2[1])
print(num1 * num2[0])
print(num1 * (num2[2] + num2[1] * 10 + num2[0] * 100))