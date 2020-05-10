def matrix_to_graph(list1):
    global number_of_nodes
    g = {}
    for i in range(number_of_nodes):
        g[i] = {}
    for i in range(number_of_nodes):
        for j in range(number_of_nodes):
            if i != j and list1[i][j] != 0:
                g[i][j] = list1[i][j]
            elif i == j:
                g[i][j] = 9999
    return g


def print_graph():
    for i in graph.keys():
        for j in graph[i].keys():
            print(i, '-->', j, '=', graph[i][j])


def visiting(node, end):
    global visited, shortest_distance, queue
    for i in graph[node].keys():
        distance_from_node = shortest_distance[node][0] + graph[node][i]
        if i not in visited and shortest_distance[i][0] > distance_from_node:
            if i not in queue:
                queue.append(i)
            shortest_distance[i] = [distance_from_node, node]
            if i == end:
                return True
    return False


def dijkstra(start, end):
    global shortest_distance, visited, queue
    shortest_distance = {}
    for i in graph.keys():
        shortest_distance[i] = [9999, i]
    shortest_distance[start] = [0, start]
    visited = []
    queue = [start]
    while queue:
        temp = [9999, 999999]
        for i in queue:
            if shortest_distance[i][0] < temp[0]:
                temp = [shortest_distance[i][0], i]
        if start != 999999:
            node = temp[1]
            queue.remove(node)
            if visiting(node, end):
                break
            visited.append(node)
        else:
            break


print("Enter adjacency matrix")
number_of_nodes = int(input("Enter number of nodes:"))
g = []
for i in range(number_of_nodes):
    g.append([int(x) for x in input().split()])
graph = matrix_to_graph(g)
print_graph()
print("graph node are:", graph.keys())
start = int(input("Enter Starting node"))
while start not in graph.keys():
    start = int(input("Enter starting node which is in graph nodes:"))
end = int(input("Enter ending node:"))
while end not in graph.keys():
    end = int(input("Enter ending node which is in graph node:"))
dijkstra(start, end)
temp = end
if shortest_distance[end][1] == end:
    print("Route not possible")
    exit()
while start != end:
    print(end, end='-')
    end = shortest_distance[end][1]
print(end)
print("Total distance = ", shortest_distance[temp][0])
