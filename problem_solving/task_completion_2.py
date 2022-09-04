"""Given a tree of tasks, each task has an ID and a time taken.
Constraints:
1. A task can be started only after its parent task is complete.
2. Sibling tasks can be run in parallel.

New constraints:
1. N cores available, so only N tasks can be run simultaneously
2. The task with lower ID will be executed first.

Find the maximum time it will take to complete all tasks.

Example (ID, units of time):
(3, 5) -> (4, 5)
       -> (9, 10) -> (1, 5)
                  -> (2, 2) -> (8, 2)
       -> (7, 11)

Assuming 2 cores:
Maximum time taken = 5 (id 3) + 5 (id 4) + 10 (id 9) +  5 (id 1) = 25
"""

from typing import List

class Task:
    def __init__(self, id: int, time: int, children: List['Task']):
        self.id = id
        self.time = time
        self.children = children

def maximum_time(task: Task) -> int:
    return 0

def main():
    task8 = Task(8, 2, None)
    task2 = Task(2, 2, [task8])
    task1 = Task(1, 5, None)
    task9 = Task(9, 10, [task1, task2])
    task4 = Task(4, 5, None)
    task7 = Task(7, 11, None)
    task3 = Task(3, 5, [task4, task9, task7])
    time = maximum_time(task3)
    print(time)

if __name__ == '__main__':
    main()