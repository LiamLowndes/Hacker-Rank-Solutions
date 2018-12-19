s = input()

#Initialize starting variables
cap = []
low = []
dig = []
newDig = ''
ans = ''

#Sort the characters into their respesctive arrays
for a in range(len(s)):
    if s[a].isalpha():
        if ord(s[a]) > 96:
            low.append(s[a])
        else:
            cap.append(s[a])
    else:
        dig.append(s[a])

low = sorted(low)
cap = sorted(cap)
dig = sorted(dig)

#Creats a string of all the odd numbers
for b in range(len(dig)):
    if int(dig[b]) % 2 == 1:
        newDig += str(dig[b])

#Adds to previous string all of the even numbers
for c in range(len(dig)):
    if int(dig[c]) % 2 == 0:
        newDig += str(dig[c])

#Adds the lowercase letters to the answer string
for d in range(len(low)):
    ans += low[d]

#Adds the uppercase letters to the answer string
for e in range(len(cap)):
    ans += cap[e]

ans += newDig
print(ans)
