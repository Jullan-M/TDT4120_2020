# !/usr/bin/python3
# coding=utf-8


def longest_decreasing_subsequence(s):
    n = len(s)
    lds = [1] * n 
    seq = []
    l = 1

    for j in range(0,n):
        k = n-1-j
        min_val = s[k]
        for i in range(k+1, n):
            bonus = s[k] > s[i]

            if lds[j] < lds[n-1-i] + bonus:
                lds[j] = lds[n-1-i] + bonus
                if bonus:
                    min_val = min(min_val, s[i])
        
        if min_val != s[k]:
            l = j
            seq.append(min_val)
    seq.append(max(s[:l+1]))
    print(lds, seq)
    return seq[::-1]

print(longest_decreasing_subsequence([8,9,7,3,6,2,5]))


# Teste på formatet (følge, riktig lengde på svar)
tests = [
    ([1], 1),
    ([1, 2], 1),
    ([1, 2, 3], 1),
    ([2, 1], 2),
    ([3, 2, 1], 3),
    ([1, 3, 2], 2),
    ([3, 1, 2], 2),
    ([1, 1], 1),
    ([1, 2, 1], 2),
    ([8, 7, 3, 6, 2, 6], 4),
    ([10, 4, 2, 1, 7, 5, 3, 2, 1], 6),
    ([3, 7, 2, 10, 3, 3, 3, 9], 2),
]


def verify(sequence, subsequence, optimal_length):
    # Test if the subsequence is actually a subsequence
    index = 0
    for element in sequence:
        if element == subsequence[index]:
            index += 1
            if index == len(subsequence):
                break

    if index < len(subsequence):
        return False, "Svaret er ikke en delfølge av følgen."

    # Test if the subsequence is decreasing
    for index in range(1, len(subsequence)):
        if subsequence[index] >= subsequence[index - 1]:
            return False, "Den gitte delfølgen er ikke synkende."

    # Test if the solution is optimal
    if len(subsequence) != optimal_length:
        return (
            False,
            "Delfølgen har ikke riktig lengde. Riktig lengde er"
            + "{:}, mens delfølgen har lengde ".format(optimal_length)
            + "{:}".format(len(subsequence)),
        )

    return True, ""


failed = False

for test, optimal_length in tests:
    answer = longest_decreasing_subsequence(test[:])
    correct, error_message = verify(test, answer, optimal_length)

    if not correct:
        failed = True
        print(
            'Feilet med feilmeldingen "{:}" for testen '.format(error_message)
            + "{:}. Ditt svar var {:}.".format(test, answer)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")