testCases = int(input())

for a in range(testCases):
    rowLen = int(input())
    cubes = input().split(" ")
    base = 0
    
    for c in range(len(cubes)):
        cubes[c] = int(cubes[c])
    
    for b in range(rowLen):

        if cubes[0] < cubes[-1]:
            side = cubes[-1]
            right = True
        else:
            side = cubes[0]
            right = False

        if (base >= side) or (base == 0):
            base = side
            if (right):
                del cubes[-1]
            else:
                del cubes[0]
        else:
            break
    
    if (len(cubes) == 0):
        print("Yes")
    else:
        print("No")
