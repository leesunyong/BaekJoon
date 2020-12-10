nums = input()
N, B, K = [int(num) for num in nums.split(' ')]

max_num = 250
min_num = 0

mat = []
max_min_mat = []

# Get Matrix
for i in range(N):
    nums = input()
    mat.append(nums)

# Get Questions
questions = []
for i in range(K):
    question = input()
    questions.append(question)


for nums in mat:
    nums = [int(num) for num in nums.split(' ')[:N]]
    max_min_row = []
    for j in range(N - B + 1):
        max_min_row.append((max(nums[j:j+B]), min(nums[j:j+B])))

    max_min_mat.append(max_min_row)


for i in range(N - B + 1):
    for j in range(N - B + 1):
        temp_max = min_num - 1
        temp_min = max_num + 1

        for k in range(i, i + B):
            if temp_max < max_min_mat[k][j][0]:
                temp_max = max_min_mat[k][j][0]
            if temp_min > max_min_mat[k][j][1]:
                temp_min = max_min_mat[k][j][1]

        max_min_mat[i][j] = temp_max - temp_min


for question in questions:
    question = [int(q) for q in question.split(' ')[:2]]
    print(max_min_mat[question[0] - 1][question[1] - 1])