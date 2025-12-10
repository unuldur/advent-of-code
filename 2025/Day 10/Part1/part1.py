#file = open("../input_test", "r")
file = open("../input.txt", "r")


machines = []
for line in file.readlines():
    datas = line.split(' ')
    machines.append({
        'objectif': datas[0][1:-1],
        'buttons': [[int(pos) for pos in data[1:-1].split(',')] for data in datas[1:-1]]
    })

print(machines)


def press_button(button, state):
    new_state = state
    for pos in button:
        new_state = new_state[:pos] + ('.' if new_state[pos] == '#' else '#') + new_state[pos+1:]
    return new_state


def parcours(buttons, objectif):
    states = dict()
    next_states = set()
    next_states.add(''.join(['.' for _ in range(len(objectif))]))
    index = 0
    while objectif not in next_states:
        new_states = set()
        for current_state in next_states:
            for button in buttons:
                new_state = press_button(button, current_state)
                if new_state in states.keys():
                    continue
                new_states.add(new_state)
                states[new_state] = index + 1
        index += 1
        next_states = new_states
    return states[objectif]


result = sum([parcours(machine['buttons'], machine['objectif']) for machine in machines])

print(result)

