from node import Node
from collections import deque
# Import the queue module
from queue import Queue

class BreadthFirstSearch:

    def breadth_first_search(map, initial, goal):
    # Create an empty queue and enqueue the initial node
        queue = Queue()
        queue.put(initial)
        # Create an empty dictionary to store the parent of each node
        parent = {}
        # Set the parent of the initial node to None
        parent[initial] = None
        # Loop until the queue is empty or the goal is found
        while not queue.empty():
            # Dequeue a node from the queue
            node = queue.get()
            # If the node is the goal, break the loop
            if node == goal:
                break
            # For each neighbor of the node that is not visited
            for neighbor in map[node]:
                if neighbor not in parent:
                    # Enqueue the neighbor and set its parent to the node
                    queue.put(neighbor)
                    parent[neighbor] = node
        # Create an empty list to store the path
        path = []
        # If the goal was found, trace back the path from the goal to the initial
        if goal in parent:
        # Start from the goal
            current = goal
        # Loop until the initial is reached
            while current != initial:
                # Add the current node to the path
                path.append(current)
                # Move to its parent
                current = parent[current]
                # Add the initial node to the path
                path.append(initial)
                # Reverse the path to get it from initial to goal
            path.reverse()
        # Return the path
        return path