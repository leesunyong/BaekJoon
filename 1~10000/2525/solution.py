hour, minute = map(int, input().split())
time = int(input())
minute += time
hour_carry = minute // 60
minute %= 60

hour = (hour + hour_carry) % 24

print(hour, minute)