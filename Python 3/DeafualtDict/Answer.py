#Create a default dictionary
from collections import defaultdict
d = defaultdict(list)

#Collect user input
temp = input().split()
n = int(temp[0])
m = int(temp[1])

#Add the letters to the dictionary as well as the position they occupy
for i in range(n):
    d[input()].append(i+1)

#Print out the positions of all the items in both B and A, if the item doesn't exist in A print -1
for j in range(m):
    
    b = input()
    
    if b in d.keys():
        
        for k in range(len(d[b])):
            print(d[b][k], end = " ")
        print()
    
    else:
        print(-1)
