#This function, when combind with the code on HackerRank, will complete the question

def repeatedString(s, n):

    a = 0
    ans = 0

    #Count how many a's are in the original string
    for i in range(len(s)):
        if s[i] == "a":
            a += 1

    repeat = n // len(s) #the amount of times the string will repeat fully
    ans += repeat * a

    end = s[:(n % len(s))] #the last part of the string that is cut off

    # loop through the shortned version of the string and count all the a's
    for j in range(len(end)):
        if end[j] == "a":
            ans += 1

    return(ans)
