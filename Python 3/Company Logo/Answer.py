#Create an ordered dictionary
from collections import OrderedDict
od = {}

#Create a dictionary where each letter maps to its opposite (a toz, b to y etc..)
alphabet = list('abcdefghijklmnopqrstuvwxyz')
alpha = {}
for i in range(26):
    alpha[alphabet[i]] = alphabet[-i - 1]


if __name__ == '__main__':

    #Creats a dictionary where the letters are they keys and the amount of times they repeat as the values
    s = list(input())
    for item in s:
        if item in od.keys():
            od[item] += 1
        else:
            od[item] = 1

    #Creats an array or arrays.  Where the first point is the number of repeats and the second is the letters opposite.  If we dont do this the numbers will sort properly but the letters would be backwards.  By doing this we make sure the letters sort properly.
    hold = []
    for key in od.keys():
        hold.append([od[key], alpha[key]])

    #Sort and reverse the array
    hold = (sorted(hold)[::-1])

    #Convert the letters back to their original state
    for pair in hold:
        pair[1] = alpha[pair[1]]
    
    #Prints the top three letters in order
    for a in range(3):
        print(hold[a][1], hold[a][0])
