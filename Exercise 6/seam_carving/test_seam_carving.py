#!/usr/bin/python3
# coding=utf-8


def find_path(weights):
    width = len(weights[0])
    height = len(weights)

    if width == 1: # Matrices with 1 column are trivial, return tuples of indexes
        return [(0, y) for y in range(height)]

    weight_sum = [[0 for _w in range(width)] for _h in range(height)] # Cumulative sum of weights
    pointers = [[-1 for _w in range(width)] for _h in range(height-1)] # Each column in rows after 1 point to to a column on the above row.

    for x in range(width):
        weight_sum[0][x] = weights[0][x]

    for y in range(1, height):
        for x in range(0, width):
            # Handle the edges gracefully
            if x == 0: # |/
                cands = [weight_sum[y-1][x], weight_sum[y-1][x+1]]
                min_val = min(cands)
                min_id = cands.index(min_val)
                weight_sum[y][x] = weight_sum[y-1][x+min_id] + weights[y][x]
                pointers[y-1][x] = x+min_id
            elif x == width-1: # \|
                cands = [weight_sum[y-1][x-1], weight_sum[y-1][x]]
                min_val = min(cands)
                min_id = cands.index(min_val)
                weight_sum[y][x] = weight_sum[y-1][x-1+min_id] + weights[y][x]
                pointers[y-1][x] = x-1+min_id
            else: # \|/
                cands = [weight_sum[y-1][x-1], weight_sum[y-1][x], weight_sum[y-1][x+1]]
                min_val = min(cands)
                min_id = cands.index(min_val)
                weight_sum[y][x] = weight_sum[y-1][x-1+min_id] + weights[y][x]
                pointers[y-1][x] = x-1+min_id
    # Find the index with the least cumulative sum on the last row. 
    s_min = min(weight_sum[height-1])
    s_id = weight_sum[height-1].index(s_min)

    path = [(s_id, height-1)]
    for y in range(height-2, -1, -1):
        s_id = pointers[y][s_id] # Pointer of the current index points to the correct path.
        path.append((s_id, y))
    return path[::-1] # Return reversed list (from top to bottom)

# Tester på formatet (vekter, minste mulige vekt på sti).
tests = [
    ([[1]], 1),
    ([[1, 1]], 1),
    ([[1], [1]], 2),
    ([[2, 1], [2, 1]], 2),
    ([[1, 1], [1, 1]], 2),
    ([[2, 1], [1, 2]], 2),
    ([[3, 2, 1], [1, 3, 2], [2, 1, 3]], 4),
    ([[1, 10, 3, 3], [1, 10, 3, 3], [10, 10, 3, 3]], 9),
    ([[1, 2, 7, 4], [9, 3, 2, 5], [5, 7, 8, 3], [1, 3, 4, 6]], 10),
]


# Verifiserer at en løsning er riktig gitt vektene, stien og den minst
# mulige vekten man kan ha på en sti.
def verify(weights, path, optimal):
    if len(path) != len(weights):
        return False, "Stien er enten for lang eller for kort."

    last = -1
    for index, element in enumerate(path):
        if type(element) != tuple:
            return False, "Stien består ikke av tupler."
        if len(element) != 2:
            return False, "Stien består ikke av tupler på formatet (x,y)."
        if index != element[1]:
            return False, "Stien er ikke vertikal."
        if element[0] < 0 or element[0] >= len(weights[0]):
            return False, "Stien går utenfor bildet."
        if last != -1 and not last - 1 <= element[0] <= last + 1:
            return False, "Stien hopper mer enn en piksel per rad."
        last = element[0]

    weight = sum(weights[y][x] for x, y in path)
    if weight != optimal:
        return (
            False,
            "Stien er ikke optimal. En optimal sti ville hatt"
            + "vekten {:}, mens din hadde vekten {:}".format(optimal, weight),
        )

    return True, ""


failed = False

for test, optimal_weight in tests:
    answer = find_path([row[:] for row in test])
    correct, error_message = verify(test, answer, optimal_weight)
    if not correct:
        failed = True
        print(
            'Feilet med feilmeldingen "{:}" for testen '.format(error_message)
            + "{:}. Ditt svar var {:}.".format(test, answer)
        )

if not failed:
    print("Koden din fungerte for alle eksempeltestene.")