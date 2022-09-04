"""Given a tree of tasks, each task has an ID and a time taken.
Constraints:
1. A task can be started only after its parent task is complete.
2. Sibling tasks can be run in parallel.

Find the maximum time it will take to complete all tasks.

Example (ID, units of time):
(3, 5) -> (4, 5)
       -> (5, 10) -> (1, 5)
                  -> (2, 2) -> (8, 2)
       -> (7, 11)

Maximum time taken = 5 + 10 + 5 = 20
"""

from typing import List

class Task:
    def __init__(self, id: int, time: int, children: List['Task']):
        self.id = id
        self.time = time
        self.children = children

def maximum_time(task: Task) -> int:
    if not task:
        return 0
    
    longest_child_time = 0
    if task.children:
        for child in task.children:
            child_time = maximum_time(child)
            if child_time > longest_child_time:
                longest_child_time = child_time
    
    return task.time + longest_child_time

def main():
    task8 = Task(8, 2, None)
    task2 = Task(2, 2, [task8])
    task1 = Task(1, 5, None)
    task5 = Task(5, 10, [task1, task2])
    task4 = Task(4, 5, None)
    task7 = Task(7, 11, None)
    task3 = Task(3, 5, [task4, task5, task7])
    time = maximum_time(task3)
    print(time)

if __name__ == '__main__':
    main()