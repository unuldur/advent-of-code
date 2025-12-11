#file = open("../input_test", "r")
file = open("../input.txt", "r")


starting_graph = dict()
for line in file:
    line = line.strip()
    start, outs = line.split(":")
    starting_graph[start] = outs.strip().split(" ")


def parcours(graph, starting_node):
    if starting_node not in graph:
        return [[starting_node]]
    paths = []
    for node in graph[starting_node]:
        for path in parcours(graph, node):
            paths.append([starting_node, *path])
    return paths

print(len(parcours(starting_graph, "you")))