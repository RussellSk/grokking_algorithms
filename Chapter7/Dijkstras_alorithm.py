# Chapter 7
# Dijkstra's algorithm implementation

# Represent weighted graph as hash table and represent weights of edges
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}  # The finish node doesn't have any neighbors

# The hash table to store costs for each node.
# The cost of a node is how long it takes to get to that node from the start.
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# The hash table for the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Array to keep track of all the nodes already processed
processed = []


def find_shortest_path():
    """This function implements Dijkstra's algorithm"""
    node = find_lowest_cost_node()  # Find the lowest-cost node that you haven't processed yed.
    while node is not None:  # If you've processed all the nodes, this while loop is done.
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # Go through all the neighbors of this node.
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:  # If it's cheaper to get to this neighbor by going through this node
                costs[n] = new_cost  # update the cost for this node.
                parents[n] = node  # This node becomes the new parent for this neighbor.
        processed.append(node)  # Mark the node as processed.
        node = find_lowest_cost_node()  # Find the next node to process, and loop.


def find_lowest_cost_node():
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # Go through each node.
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # If it's the lowest cost so far and hasn't been processed yet
            lowest_cost = cost  # Set it as the new lowest-cost node.
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == "__main__":
    find_shortest_path()
    print("Cost from the start to each node:")
    print(costs)
    print("Shortest path:")
    print(parents)
