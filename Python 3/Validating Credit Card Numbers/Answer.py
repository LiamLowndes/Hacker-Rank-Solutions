import re
import sys

def valid_credit(credit):

    temp = credit.split("-")
    credit = ''

    #Checks if the credit card is in groups of 4 sepereated by a "-" or has no seperation at all
    if len(temp) == 4 or len(temp) == 1:
        pass
    else:
        return("Invalid")

    #Checks to see that each part has either 4 parts of 4 or one part of 16
    for part in temp:
        if len(part) == 4 or len(part) == 16:
            credit += part
        else:
            return("Invalid")

    #Checks for any invalid charaters
    if (re.search('[a-zA-z\s_!@#$%^&]', credit) != None):
        return("Invalid")
    #Checks that the first num is inbetween 4 and 6 (inclusive)
    if int(credit[0]) < 4 or int(credit[0]) > 6:
        return("Invalid")
    #Checks to make sure length is 16
    if len(credit) != 16:
        return("Invalid")
    #Checks for a digit that repeats more than 3 times
    if (re.search(r'(\d)\1{3}', credit) != None):
        return("Invalid")
    
    return("Valid")

#Takes the input and tests the credit card numbers with the above function
n = int(input())
for a in range(n):
    credit_num = input()
    sys.stdout.write(valid_credit(credit_num) + "\n")
