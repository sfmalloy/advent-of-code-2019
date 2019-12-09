p = list(map(int, open("5.in", 'r').read().strip().split(',')))
q = p.copy()

add = 1
mult = 2
readin = 3
out = 4
halt = 99

i = 0
opcode = 0
output = 0
user_input = 1
while (opcode != halt):
    instr = p[i]
    opcode = p[i] % 100
    instr = instr // 100
    param_modes = [int(x) for x in str(instr)]
    param_modes.reverse()
    
    while (len(param_modes) < 3):
        param_modes.append(0)
    
    if (opcode != halt):
        if (opcode == add or opcode == mult):
            a = p[i + 1] if param_modes[0] == 1 else p[p[i + 1]]
            b = p[i + 2] if param_modes[1] == 1 else p[p[i + 2]]
            pos = p[i + 3] 
            
            p[pos] = a + b if opcode == add else a * b
            i += 4
        elif (opcode == readin):
            p[i + 1 if param_modes[0] == 1 else p[i + 1]] = user_input
            i += 2
        elif (opcode == out):
            output = p[i + 1] if param_modes[0] == 1 else p[p[i + 1]]
            i += 2
print("Part 1: %d" % output)

p = q.copy()

jump_if_true = 5
jump_if_false = 6
less_than = 7
equals = 8

i = 0
opcode = 0
output = 0
user_input = 5
while (opcode != halt):
    instr = p[i]
    opcode = p[i] % 100
    instr = instr // 100
    param_modes = [int(x) for x in str(instr)]
    param_modes.reverse()
    
    while (len(param_modes) < 3):
        param_modes.append(0)

    if (opcode != halt):
        a = p[i + 1] if param_modes[0] == 1 else p[p[i + 1]]
        b = pos = 0
        
        if (opcode in [add, mult, less_than, equals, jump_if_true, jump_if_false]):
            b = p[i + 2] if param_modes[1] == 1 else p[p[i + 2]]
        if (opcode in [add, mult, less_than, equals]):
            pos = p[i + 3]

        if (opcode == add or opcode == mult):
            if (opcode == add):
                p[pos] = a + b
            else:
                p[pos] = a * b
            i += 4
        elif (opcode == readin):
            if (param_modes[0] == 1):
                pos = i + 1
            else:
                pos = p[i + 1]
            p[pos] = user_input
            i += 2
        elif (opcode == out):
            output = a
            i += 2
        elif (opcode == jump_if_true or opcode == jump_if_false):
            if ((opcode == jump_if_true and a != 0) or (opcode == jump_if_false and a == 0)):
                i = b
            else:
                i += 3
        elif (opcode == less_than or opcode == equals):
            if ((opcode == less_than and a < b) or (opcode == equals and a == b)):
                p[pos] = 1
            else:
                p[pos] = 0
            i += 4

print("Part 2: %d" % output)
