def schulze_method(A):
    n = len(A)
    path = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(1+i,n):
            if A[i][j] > A[j][i]:
                path[i][j] = A[i][j]
                path[j][i] = 0
            elif A[i][j] < A[j][i]:
                path[j][i] = A[j][i]
                path[i][j] = 0
    
    for k in range(0, n):
        for i in range(0,n):
            if k != i:
                for j in range(0, n):
                    if k != j and i != j:
                        path[i][j] = max(path[i][j], min(path[i][k], path[k][j]))

    res = [0] * n # Ordering of candidates [0,...,n-1]
    pos = [n-1] * n # Position of every candidate in res
    for i in range(0, n):
        for j in range(1+i, n):
            # If candidate i is preferred over j or if i and j have equal amount of preferation
            # then i comes before j.
            if path[i][j] >= path[j][i]: 
                pos[i] -= 1
            else:
                pos[j] -= 1
        res[pos[i]] = i
    return res



from copy import deepcopy

tests = [
    ([[0]], [0]),
    ([[0, 1], [3, 0]], [1, 0]),
    (
        [
            [0, 4, 1, 5, 5],
            [2, 0, 2, 8, 3],
            [4, 2, 0, 8, 3],
            [6, 2, 5, 0, 2],
            [11, 4, 2, 1, 0],
        ],
        [2, 4, 1, 3, 0],
    ),
    (
        [
            [0, 2, 5, 4, 3],
            [7, 0, 7, 5, 5],
            [4, 2, 0, 6, 2],
            [5, 4, 3, 0, 5],
            [6, 4, 7, 4, 0],
        ],
        [1, 4, 0, 2, 3],
    ),
    (
        [
            [0, 20, 26, 30, 22],
            [25, 0, 16, 33, 18],
            [19, 29, 0, 17, 24],
            [15, 12, 28, 0, 14],
            [23, 27, 21, 31, 0],
        ],
        [4, 0, 2, 1, 3],
    ),
]


def generate_feedback(test, expected, student):
    feedback = ""
    feedback += "Koden din feilet for input\n"
    feedback += str(test) + "\n"
    feedback += "Ditt svar er\n"
    feedback += str(student) + ",\n"
    feedback += "men riktig svar er\n"
    feedback += str(expected) + "."
    return feedback


for test, expected in tests:
    unchanged_input = deepcopy(test)
    student = schulze_method(test)
    n = len(unchanged_input)
    assert (
        len(student) == n
    ), "Listen din inneholder ikke riktig antall kandidater"
    for i in range(n):
        assert student[i] == expected[i], generate_feedback(
            unchanged_input, expected, student
        )

print("Koden din passerte alle testene.")