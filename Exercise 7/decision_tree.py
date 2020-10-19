from heapq import heappush, heappop, heapify

class Node:
    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.character = None
        self.prob = None

    def __str__(self):
        return (
            f'{{ "left_child": {self.left_child}, "right_child": {self.right_child}, "character": '
            + (
                '"' + self.character + '"'
                if self.character is not None
                else "None"
            )
            + "}"
        )
    
    def __lt__(self, other):
        return self.prob < other.prob

    @classmethod
    def from_dict(cls, dic):
        node = Node()
        if dic["left_child"] is not None:
            node.left_child = Node.from_dict(dic["left_child"])
        if dic["right_child"] is not None:
            node.right_child = Node.from_dict(dic["right_child"])
        node.character = dic["character"]
        return node

def huffman(decisions):
    n = len(decisions)

    queue = [Node() for _ in range(n)]
    for i in range(n):
        queue[i].character = decisions[i][0]
        queue[i].prob = decisions[i][1]
    
    
    heapify(queue)
    for i in range(n-1):
        p = Node()
        x = heappop(queue)
        y = heappop(queue)
        p.left_child, p.right_child = x, y
        p.prob = x.prob + y.prob
        heappush(queue, p)
    
    return heappop(queue)

def traverse(node, data, code):
    if node.character:
        data[node.character] = code
        return

    if node.left_child:
        traverse(node.left_child, data, code + "0")
    if node.right_child:
        traverse(node.right_child, data, code + "1")


def encoding(node):
    data = {}
    code = ""

    traverse(node, data, code)
    return data


def build_decision_tree(decisions):
    root = huffman(decisions)
    return encoding(root)

tests = [
    ([("a", 0.5), ("b", 0.5)], 1),
    ([("a", 0.99), ("b", 0.01)], 1),
    ([("a", 0.5), ("b", 0.25), ("c", 0.25)], 1.5),
    ([("a", 0.33), ("b", 0.33), ("c", 0.34)], 1.66),
    ([("a", 0.25), ("b", 0.25), ("c", 0.25), ("d", 0.25)], 2),
    ([("a", 0.4), ("b", 0.2), ("c", 0.2), ("d", 0.2)], 2),
    ([("a", 0.3), ("b", 0.25), ("c", 0.25), ("d", 0.2)], 2),
    ([("a", 0.3), ("b", 0.2), ("c", 0.2), ("d", 0.2), ("e", 0.1)], 2.3),
]


def check_overlap_and_add_to_tree(tree, value):
    is_valid = len(tree) == 0
    for v in value:
        if v in tree:
            tree = tree[v]
        else:
            if len(tree) == 0 and not is_valid:
                return False
            tree[v] = {}
            tree = tree[v]
            is_valid = True

    return is_valid


def test_answer(student, test_case, correct_answer):
    if len(test_case) <= 20:
        feedback = "Feilet for tilfellet {:}.".format(
            test_case
        ) + " Ditt svar var {:}.\n".format(student)
    else:
        feedback = "Koden returnerte et galt svar:\n"

    if not isinstance(student, dict):
        feedback += "Funksjonen skal returnere en oppslagstabell (dictionary)."
        print(feedback)
        return False

    tree = {}
    expectance = 0
    for value, prob in test_case:
        if value not in student:
            feedback += "Beslutningen {:} er ikke med i treet.".format(value)
            print(feedback)
            return False

        encoding = student[value]
        if not isinstance(encoding, str) or not set(encoding) <= {"1", "0"}:
            feedback += (
                "Hver beslutning skal ha en streng av nuller og "
                + "enere knyttet til seg. "
            )
            print(feedback)
            return False

        if not check_overlap_and_add_to_tree(tree, encoding):
            feedback += "En av beslutningene er en internnode."
            print(feedback)
            return False

        expectance += prob * len(encoding)

    if expectance > correct_answer + 0.0000001:
        feedback += (
            "Beslutningstreet ditt er ikke optimalt. Det skulle "
            + "hatt en forventning på {:}".format(correct_answer)
            + " spørsmål, men har en forventning på "
            + str(expectance)
        )
        print(feedback)
        return False

    return True


passed = True
for test_case, answer in tests:
    student = build_decision_tree(test_case)
    passed &= test_answer(student, test_case, answer)

if passed:
    print("Passerte alle testene")