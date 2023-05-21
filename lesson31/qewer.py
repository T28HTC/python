input()
cam = input()
kamushek = list(cam)
perehod = 0
a = 0
while perehod < len(kamushek) - 1:
    if kamushek[perehod] == kamushek[perehod + 1]:
        kamushek.pop(perehod)
        a+=1
    else:
        perehod+=1
print(a)