# Solve_Problem
1. Design a binary tree and then write an algorithm to print the least(nearest) two common parent(if 2 parents exist otherwise 1  common parent) node between 2 nodes of a binary tree for given 2 key values which are present in binary tree.
Input  :  If below tree and values 1 and 5 given

Output : 2

Input  :  If below tree and values 3 and 6 given

Output : 2 

Input  :  If below tree and values 4 and 6 given

Output : 2 and 3


2. A string of lowercase characters in range ascii[‘a’..’z’]. We want to reduce the string to its shortest length by doing a series of operations. In each operation we select a pair of adjacent lowercase letters that match, and delete them. For instance, the string aab could be shortened to b in one operation. Now we have to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String
Function Description

Complete the MaxReducedString function. It should return the super reduced string or Empty String if the final string is empty.

superReducedString has the following parameter(s):

s: a string to reduce

Output Format:
If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

Example:
aaabccddd will get reduced to→ abccddd  will get reduced to → abddd  will get reduced to → abd
