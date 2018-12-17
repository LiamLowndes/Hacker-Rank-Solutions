text = input()

ans = []

while (len(text) > 0):
    
    count = 1
    num = int(text[0])

    while(True):
        
        if (count) > (len(text)-1):
            break
        
        if num == int(text[count]):
            count += 1
        else:
            break
    
    ans.append((count, num))
    
    for b in range(count):
        text = text[1:]
    
for a in range(len(ans)):
    print (ans[a], end=" ")
