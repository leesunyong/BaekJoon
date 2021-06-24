import math

a, b, c, = map(int, input().split())
d = math.sqrt(b**2 + c**2)

print(math.floor(a / d * b), math.floor(a / d * c))