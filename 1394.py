if __name__ == '__main__':
    char_set = input()
    password = input()

    result = 0
    length = len(char_set)
    base = 1

    char2idx = {}
    for i, c in enumerate(char_set):
        char2idx[c] = i + 1
    
    i = len(password) - 1
    while i >= 0:
        result += char2idx[password[i]] * base

        base *= length
        
        if base > 900528:
            base %= 900528

        i -= 1

    result %= 900528
    print(result)
