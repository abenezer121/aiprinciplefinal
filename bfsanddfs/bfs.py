
from collections import deque
# Import the queue module
from queue import Queue

class BreadthFirstSearch:

    def breadth_first_search(map, initial, goal):
        queue = Queue()
        queue.put(initial)
        parent = {}
      
        parent[initial] = None
        while not queue.empty():
            node = queue.get()
            if node == goal:
                break
            for neighbor in map[node]:
                if neighbor not in parent:
                    queue.put(neighbor)
                    parent[neighbor] = node
        path = []
        if goal in parent:
            current = goal
            while current != initial:
                path.append(current)
                current = parent[current]
                path.append(initial)
            path.reverse()
        return path