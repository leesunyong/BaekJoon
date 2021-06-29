hour, minute, second = map(int, input().split())
time = int(input())

second += time

minute += second // 60
second %= 60

hour += minute // 60
minute %= 60

hour %= 24

print(hour, minute, second)