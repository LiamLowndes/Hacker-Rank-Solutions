## DefaultDict

The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words belonging to word group B. For each words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.

### Constraints

1 <= n <= 10000
1 <= m <= 100
1 <= length of each word in the input <= 100

### Input Format

The first line contains integers, n and m separated by a space.

The next n lines contains the words belonging to group A.

The next m lines contains the words belonging to group B.

### Output Format

Output m lines.
The i'th line should contain the 1-indexed positions of the occurrences of the i'th word separated by spaces.

Link to the problem on Hacker Rank: [DefaultDict](https://www.hackerrank.com/challenges/defaultdict-tutorial)

Created by: [sandyeep](https://www.hackerrank.com/profile/sandyeep)
