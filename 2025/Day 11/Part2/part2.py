#file = open("../input_test_part2", "r")
file = open("../input.txt", "r")


starting_graph = dict()
for line in file:
    line = line.strip()
    start, outs = line.split(":")
    starting_graph[start] = outs.strip().split(" ")


def parcours(graph, starting_node, have_fft, have_dac, visited_note):
    if starting_node not in graph:
        return 1 if have_fft and have_dac else 0
    result = 0
    for node in graph[starting_node]:
        if (node, have_fft, have_dac) not in visited_note:
            result += parcours(graph, node, node == "fft" or have_fft, node == "dac" or have_dac, visited_note)
        else:
            result += visited_note[(node, have_fft, have_dac)]
    visited_note[(starting_node, have_fft, have_dac)] = result
    return result

print(parcours(starting_graph, "svr", False, False, {}))