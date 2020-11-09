# !/usr/bin/python3
# coding=utf-8
import math
from heapq import heapify, heappop, heappush

class Node:
    def __init__(self, name : str):
        self.id = name
        self.parent = None
        self.d = math.inf
        self.adj = []

    def __lt__(self, other):
        return self.d < other.d

def dijkstra(mat, timetable, start):
    # Initialize-Single-Source
    for a, b, t1, t2 in timetable:
        if not (a in mat):
            mat[a] = Node(a)
        if not (b in mat):
            mat[b] = Node(b)
        mat[a].adj.append((mat[b], t1, t2))
    mat[start].d = 0
    
    node_heap = [mat[start]]
    done = set()
    heapify(node_heap)

    while node_heap:
        u = heappop(node_heap)
        done.add(u)
        for v, t1, t2 in u.adj:
            # Relax
            if v.d > t2 and u.d <= t1:
                v.d = t2
                v.parent = u
                if not (v in done):
                    heappush(node_heap, v)

def earliest_arrival(timetable, start, goal):
    mat = {}
    dijkstra(mat, timetable, start)
    return mat[goal].d



tests = [
    (([("A", "B", 100, 101)], "A", "B"), 101),
    (([("B", "A", 20, 30), ("B", "A", 25, 29)], "B", "A"), 29),
    (
        ([("A", "B", 0, 10), ("B", "C", 10, 20), ("A", "C", 0, 30)], "A", "C"),
        20,
    ),
    (
        (
            [("A", "B", 0, 10), ("B", "C", 10, 20), ("A", "C", 10, 15)],
            "A",
            "C",
        ),
        15,
    ),
    (
        (
            [("A", "C", 10, 30), ("B", "C", 15, 25), ("A", "B", 0, 20)],
            "A",
            "C",
        ),
        30,
    ),
    (
        (
            [("A", "B", 10, 30), ("B", "C", 15, 25), ("B", "C", 35, 50)],
            "A",
            "C",
        ),
        50,
    ),
    (
        (
            [("A", "B", 10, 30), ("B", "C", 30, 40), ("B", "C", 35, 50)],
            "A",
            "C",
        ),
        40,
    ),
    (
        (
            [("Y", "C", 43, 98), ("C", "Y", 17, 61), ("Y", "C", 13, 18)],
            "Y",
            "C",
        ),
        18,
    ),
    (([("T", "M", 93, 97)], "T", "M"), 97),
    (
        (
            [
                ("G", "Z", 62, 79),
                ("P", "Z", 96, 98),
                ("G", "P", 87, 96),
                ("G", "P", 1, 52),
                ("G", "P", 66, 93),
            ],
            "G",
            "Z",
        ),
        79,
    ),
    (
        (
            [
                ("B", "X", 48, 97),
                ("X", "Q", 1, 19),
                ("B", "X", 22, 42),
                ("X", "Q", 2, 35),
                ("B", "X", 63, 78),
            ],
            "B",
            "X",
        ),
        42,
    ),
    (([("W", "R", 41, 58)], "W", "R"), 58),
    (
        (
            [
                ("U", "L", 53, 58),
                ("U", "A", 68, 88),
                ("L", "U", 80, 82),
                ("U", "L", 47, 90),
            ],
            "U",
            "L",
        ),
        58,
    ),
    (([("O", "X", 44, 73)], "O", "X"), 73),
    (
        (
            [
                ("D", "R", 64, 80),
                ("D", "X", 24, 59),
                ("D", "X", 25, 90),
                ("D", "R", 33, 84),
                ("R", "D", 72, 83),
            ],
            "D",
            "R",
        ),
        80,
    ),
    (
        (
            [
                ("X", "P", 32, 95),
                ("X", "P", 89, 99),
                ("X", "P", 28, 93),
                ("P", "X", 76, 96),
            ],
            "P",
            "X",
        ),
        96,
    ),
    (
        (
            [("G", "Y", 22, 94), ("L", "G", 7, 61), ("G", "Y", 96, 98)],
            "G",
            "Y",
        ),
        94,
    ),
]

failed = False

for test_case, answer in tests:
    timetable, start, goal = test_case
    student = earliest_arrival(timetable, start, goal)
    if student != answer:
        failed = True
        response = (
            "Koden feilet for følgende input: "
            + "(timetable={:}, start={:}, ".format(timetable, start)
            + "goal={:}). Riktig svar: {:}. ".format(goal, answer)
            + "Din output: {:}.".format(student)
        )
        print(response)
        break

if not failed:
    print("Koden fungerte for alle eksempeltestene.")