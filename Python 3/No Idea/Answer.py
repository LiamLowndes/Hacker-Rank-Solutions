#Takes an array and converts it into a dictionary.  Where they key is a number and its value is the amount of times it appeared in the array.
def make_dict(oldAr):

    temp = {}

    for a in oldAr:
        if a in temp.keys():
            temp[a] += 1
        else:
            temp[a] = 1
    return(temp)

#Take the input and convert the data into arrays
temp = input()
tempAr = input().split(" ")
tempA = input().split(" ")
tempB = input().split(" ")

#Converts the arrays to compressed dictionaries
ar = make_dict(tempAr)
A = make_dict(tempA)
B = make_dict(tempB)

#Checks to see which sets the numbers are in and calculates happiness
happy = 0
for item in ar.keys():
    if item in A:
        happy += A[item] * ar[item]
    if item in B:
        happy -= B[item] * ar[item]

print(happy)
