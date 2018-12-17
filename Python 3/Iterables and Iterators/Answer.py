from itertools import combinations

num = int(input())
letters = input().split()
ir = int(input())
count = 0

l = ''
for a in range(num):
    l += letters[a]

ar = (list(combinations(l, ir)))

for b in range(len(ar)):
    for c in range(ir):
        if (ar[b][c] == 'a'):
            count += 1
            break
print(count/len(ar))
