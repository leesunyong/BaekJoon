def get_sort(v, seq):
    if len(seq) == 0:
        return [v]
    if len(seq) == 1:
        if v == seq[0] - 1:
            return []
        else :
            return [v, seq[0]]

    else :
        v_prev = -1
        for i, value in enumerate(seq):
            if value == v + 1:
                continue
            if v_prev < value:
                v_prev = value
            elif v_prev == value:
                continue
            answer = get_sort(value, [*seq[:i], *seq[i+1:]])

            if len(answer) != 0:
                return [v, *answer]

        return []


if __name__ == '__main__':
    N = int(input())
    nums = [int(i) for i in input().split(' ')]
    nums.sort()

    v_prev = -1
    for i, v in enumerate(nums):

        if v_prev < v:
            v_prev = v
        elif v_prev == v:
            continue
        answer = get_sort(v, [*nums[:i], *nums[i+1:]])

        if len(answer) != 0:
            for a in answer:
                print(a, end=' ')
            
            print('\n')
            break
                