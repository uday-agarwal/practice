"""Practice problem which uses two min-heaps.

Problem:
You are given two 0-indexed integer arrays: servers and tasks of lengths n and m respectively. 
servers[i] is the weight of the ith server, and tasks[j] is the time needed to process the ith task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.
At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). 
As long as there are free servers and the queue is not empty, the task in the front of the queue will be 
assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server 
with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately 
assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue 
will be assigned in order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].
Build an array ans of length m, where ans[j] is the index of the server the jth task will be assigned to.
Return the array ans.
========================================
Examples:
Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]

Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
Output: [1,4,1,4,1,3,2]

https://leetcode.com/problems/process-tasks-using-servers/

========================================
Approach:
 - Min-heap of available servers, ordered by their weight (and second order - index)
    - to see which server to be picked up first for the next task
 - Min-heap of busy servers, ordered by their next available time
    - to see which server will be freed up first

Steps:
1. Build the available server heap
    - For each server in the list, insert (weight, index) into the heap
2. While loop - every iteration is the next time instant when a server is free:
    - while busy server heap is non empty:
        - If time == top of busy server heap:
            - Pop the top of the heap
            - Insert the popped server's (weight, index) into available server heap
    - while available server heap is non empty, 
            there are tasks with start time < current time, and
            not all tasks are processed:
        - Pop the top of the available server heap
        - Insert tuple ((current time + task time), server index) into busy server heap
        - Append (server index) to the output list
        - Increment task index which is processed
    - If available server not empty:
        Increment time by 1
      else:
        Set time = top of busy server heap
3. Return output list

Complexity (n servers, m tasks):
 - Building available server heap: O(n)
 - For each task to process: Pop from available heap, push to busy heap: O(log n) + O(log n)
 - Once each task complete: Pop from busy heap, push to available heap: O(log n) + O(log n)
 - Busy server heap is O(log n) because atmost n servers are available.
 - Overall: O(n + mlogn)
"""

from heapq import heapify, heappush, heappop
from typing import List

def assign_tasks(servers: List[int], tasks: List[int]) -> List[int]:
    assigned_servers = [-1 for _ in range(len(tasks))]
    available_servers = [(weight, index) for (index, weight) in enumerate(servers)]
    heapify(available_servers)

    busy_servers = []

    seconds = 0
    task_index = 0
    while task_index < len(tasks):
        # Free up servers for completed tasks
        while busy_servers and seconds == busy_servers[0][0]:
            _, earliest_available = heappop(busy_servers)
            heappush(available_servers, (servers[earliest_available], earliest_available))

        # Assign new tasks
        while available_servers and task_index <= seconds and task_index < len(tasks):
            _, lowest_weight_index = heappop(available_servers)
            heappush(busy_servers, ((seconds + tasks[task_index]), lowest_weight_index))
            assigned_servers[task_index] = lowest_weight_index
            task_index += 1

        if available_servers:
            seconds += 1
        else:
            seconds = busy_servers[0][0]

    return assigned_servers

def main():
    servers = assign_tasks(servers = [3,3,2], tasks = [1,2,3,2,1,2])
    print(servers)

    servers = assign_tasks(servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1])
    print(servers)

if __name__ == "__main__":
    main()
