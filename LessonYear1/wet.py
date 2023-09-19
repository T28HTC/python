c = 0
oper = {
    "add": lambda x: c + x,
    "mul": lambda x: c * x,
    "minus": lambda x: c - x,
    "div": lambda x: c // x,
}

while True:
    comm = input().split()
    if len(comm) == 1:
        comm = comm[0]
        if comm == "result":
            print(c)
        elif comm == "zero":
            c = 0
        elif comm == "exit":
            break
    else:
        oper[comm[0]](int(comm[1]))
