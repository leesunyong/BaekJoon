N = int(input())

five = N // 5 + 1
three = 0
while five >= 0:
    if five * 5 + three * 3 == N:
        print(five + three)
        break
    elif five * 5 + three * 3 > N:
        five -= 1
    else :
        three +=1

if five < 0:
    print(-1)