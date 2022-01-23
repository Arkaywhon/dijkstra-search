from queue import PriorityQueue

graphB = {
    '1': [(3, '3'), (3, '4'), (2, '5')],
    '2': [(2, '3'), (3, '7'), (1, '4')],
    '3': [(3, '1'), (2, '2')],
    '4': [(3, '1'), (1, '2'), (2, '6')],
    '5': [(2, '1')],
    '6': [(2, '4'), (2, '8')],
    '7': [(3, '2'), (1, '8')],
    '8': [(2, '6'), (1, '7')],
}


# Implementation of Dijkstra's search algorithm (best first search).
def best_first_search(graph, start_node, goal_node):

    priority_queue = PriorityQueue()
    priority_queue.put((0, start_node))

    reached = {start_node: 0}
    previous_nodes = {}

    while priority_queue.queue:
        weight, node = priority_queue.get()
        print('Exploring node', node, 'with weight', weight)

        if node == goal_node:
            return construct_path(previous_nodes, goal_node)

        for adj_weight, adj_node in graphB[node]:
            new_weight = weight + adj_weight

            if (adj_node not in reached) or (new_weight < reached[adj_node]):
                reached[adj_node] = new_weight
                previous_nodes[adj_node] = node
                priority_queue.put((new_weight, adj_node))

    return []


def construct_path(previous_nodes, goal_node):

    current_node = goal_node
    path = [current_node]

    while current_node in previous_nodes:
        prior_node = previous_nodes[current_node]
        path.append(prior_node)
        current_node = prior_node

    path.reverse()
    return path


start = '1'
goal = '6'

shortest_path = best_first_search(graphB, start, goal)

print('The shortest path between nodes', start, 'and', goal, 'is:', shortest_path)
