# !/usr/bin/python3
# coding=utf-8


import random

def building_time_aux(node, visited, tot_time):
    visited[node.i] = True
    q = node.time # Time it takes to finish current task
    p = 0 # Recursive max time of neighbor nodes
    for nbor in node.depends_on:
        if not visited[nbor.i]:
            p = max(p, building_time_aux(nbor, visited, tot_time))
        else:
            p = max(p, tot_time[nbor.i])
    tot_time[node.i] = q + p
    return q + p

def building_time(tasks):
    V = len(tasks)
    visited = [False] * V
    tot_time = [0] * V
    
    q = -1
    for node in tasks:
        if not visited[node.i]:
            q = max(q, building_time_aux(node, visited, tot_time))
    return q




class Task:
    def __init__(self, time, depends_on, i):
        self.time = time
        self.depends_on = depends_on
        self.i = i

    def __str__(self):
        depends_on_str = ", ".join(
            "Task " + str(task.i) for task in self.depends_on
        )
        return "Task {:}: {{time: {:}, depends_on: ".format(
            self.i, self.time
        ) + "[{:}]}}".format(depends_on_str)

    def __repr__(self):
        return str(self)


def test_case_from_list(tasks_arr):
    tasks = [Task(task[0], [], i) for i, task in enumerate(tasks_arr)]
    for i in range(len(tasks_arr)):
        for j in tasks_arr[i][1]:
            tasks[i].depends_on.append(tasks[j])
    random.shuffle(tasks)
    return tasks


tests = [
    ([(4, [])], 4),
    ([(1, []), (4, [2]), (5, [])], 9),
    ([(3, [])], 3),
    ([(2, [1, 2]), (1, [2]), (4, [])], 7),
    ([(4, [])], 4),
    ([(4, [])], 4),
    ([(1, [])], 1),
    ([(1, [1]), (3, [])], 4),
    ([(1, [1]), (3, [2]), (3, [])], 7),
    ([(2, [2, 3]), (3, [3]), (3, [3]), (5, [])], 10),
]

random.seed(123)

failed = False

for test_case, answer in tests:
    test_case = test_case_from_list(test_case)
    student = building_time(test_case)
    if student != answer:
        failed = True
        response = "Koden feilet for følgende input: (tasks={:}). ".format(
            test_case
        ) + "Din output: {:}. Riktig output: {:}".format(student, answer)
        print(response)
        break

if not failed:
    print("Koden fungerte for alle eksempeltestene.")