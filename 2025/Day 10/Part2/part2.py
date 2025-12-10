import sympy as sp
import pulp

#file = open("../input_test", "r")
file = open("../input.txt", "r")



machines = []
for line in file.readlines():
    datas = line.strip().split(' ')
    machines.append({
        'buttons': [[int(pos) for pos in data[1:-1].split(',')] for data in datas[1:-1]],
        'joltage': tuple([int(pos) for pos in datas[-1][1:-1].split(',')])
    })

print(machines)


def solve(buttons, joltage):
    prob = pulp.LpProblem("Minimize_xi_sum", pulp.LpMinimize)

    xs = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(buttons))]

    for i, j in enumerate(joltage):
        prob += sum(xs[b] for b, button in enumerate(buttons) if i in button) == j

    prob += sum(xs)
    prob.solve()
    return sum(v.value() for v in xs)


result = sum([solve(machine['buttons'], machine['joltage']) for machine in machines])

print(result)

