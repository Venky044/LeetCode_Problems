"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of commands 
where each command will be of the  types listed above. Iterate through each 
command in order and perform the corresponding operation on your list.

i/p:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

o/p:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""


N = int(input())
result = []
for _ in range(N):
    opcmd, *num = input().split()
    if opcmd == 'print':
        print(result)
    else:
        exp = ','.join(num)
        eval(f'result.{opcmd}({exp})')
