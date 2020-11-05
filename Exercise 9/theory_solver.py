# !/usr/bin/python3
# coding=utf-8

class Variable:
    def __init__(self, name : str):
        self.name = name
        self.parent = self
        self.rank = 0

    def new_parent(self, other):
        self.parent = other
        if self.rank == other.rank:
            other.rank += 1

    def link(self, other):
        if self.rank > other.rank:
            other.parent = self
        else:
            self.parent = other
            if self.rank == other.rank:
                other.rank += 1
    
    def find_parent(self):
        if self.parent != self:
            self.parent = self.parent.find_parent()
        return self.parent

    def union(self, other):
        self.find_parent().link(other.find_parent())

# Returns True if there is a cycle
def dfs(nodes, edges):
    closed_nodes = set()
    active_nodes = set()
    for node in nodes:
        if dfs_visit(node, edges, active_nodes, closed_nodes):
            return True
    return False

def dfs_visit(node, edges, active_nodes, closed_nodes):
    if node in closed_nodes:
        return False
    if node in active_nodes:
        return True
    active_nodes.add(node)
    for n in edges[node]:
        if dfs_visit(n, edges , active_nodes , closed_nodes ):
            return True
    active_nodes.remove(node)
    closed_nodes.add(node)

def check(variables, constraints):
    n = len(variables)
    vars_ = {x: Variable(x) for x in variables}
    for a, s, b in constraints:
        v1, v2 = vars_[a], vars_[b]
        if s == "=" and v1.find_parent() != v2.find_parent():
            v1.union(v2)
    
    nodes = set([var.find_parent().name for var in vars_.values()])
    edges = {node: set() for node in nodes}
    for a, s, b in constraints:
        v1, v2 = vars_[a], vars_[b]
        if s == "<":
            edges[v1.find_parent().name].add(v2.find_parent().name)
        elif s == ">":
            edges[v2.find_parent().name].add(v1.find_parent().name)
    return not dfs(nodes, edges)


 

tests = [
    ((["x1"], []), True),
    ((["x1", "x2"], [("x1", "=", "x2")]), True),
    ((["x1"], [("x1", ">", "x1")]), False),
    ((["x1"], [("x1", "=", "x1")]), True),
    ((["x1", "x2"], [("x1", "<", "x2")]), True),
    ((["x1", "x2"], [("x2", "<", "x1"), ("x1", "=", "x2")]), False),
    ((["x1", "x2"], [("x2", ">", "x1"), ("x1", "<", "x2")]), True),
    ((["x1", "x2"], [("x1", ">", "x2"), ("x2", ">", "x1")]), False),
    (
        (
            ["x1", "x2", "x3"],
            [("x1", "<", "x2"), ("x2", "<", "x3"), ("x1", ">", "x3")],
        ),
        False,
    ),
    (
        (
            ["x1", "x2", "x3"],
            [("x1", "<", "x2"), ("x3", "=", "x1"), ("x2", "<", "x3")],
        ),
        False,
    ),
    ((["x4", "x0", "x1"], [("x1", "<", "x0")]), True),
    ((["x5", "x8"], [("x8", "<", "x5"), ("x8", "<", "x5")]), True),
    ((["x1", "x0", "x2"], []), True),
    (
        (
            ["x4", "x8", "x5"],
            [("x4", "<", "x5"), ("x8", ">", "x5"), ("x5", "<", "x8")],
        ),
        True,
    ),
    (
        (
            ["x5", "x9", "x0"],
            [
                ("x9", ">", "x5"),
                ("x9", "=", "x0"),
                ("x0", "=", "x9"),
                ("x0", "=", "x9"),
            ],
        ),
        True,
    ),
    (
        (
            ["x0", "x6", "x7"],
            [("x7", "=", "x0"), ("x7", ">", "x0"), ("x6", ">", "x0")],
        ),
        False,
    ),
    ((["x8", "x6", "x0"], []), True),
    (
        (
            ["x8", "x7", "x0"],
            [("x8", "=", "x0"), ("x0", "=", "x8"), ("x0", "=", "x8")],
        ),
        True,
    ),
    (
        (
            ["x8", "x4"],
            [
                ("x4", ">", "x8"),
                ("x4", ">", "x8"),
                ("x8", "<", "x4"),
                ("x4", ">", "x8"),
                ("x8", "=", "x4"),
            ],
        ),
        False,
    ),
    ((["x3", "x8", "x5"], [("x3", ">", "x8")]), True),
]


for test_case, answer in tests:
    variables, constraints = test_case
    student = check(variables, constraints)
    if student != answer:
        response = (
            "Koden feilet for følgende input: "
            + "(variables={:}, constraints={:}). ".format(variables, constraints)
            + "Din output: {:}. Riktig output: {:}".format(student, answer)
        )
        print(response)
        break