"""
   Write a program to find the count or occurence of substring 
in a main string with time complexity O(n).
"""

import re

main_string = "byehelloAmericahelllhelloAmericahelAmericahello"

sub_string = input("enter a sub string: ")

match_string = re.findall(sub_string, main_string, re.I)

no_of_occurence = len(match_string)
print(no_of_occurence)


"""
OUTPUT:
>>> enter a sub string: hello
3
"""
# -------------------------------------------------


# Another way to solving the above problem

# main_string = "byehelloAmericahelllhelloAmericahelAmericahello"
# sub_string = input("enter a sub string: ")

count = 0
for i in range(len(main_string)):
    if main_string[i] == sub_string[0]:
        if main_string[i : (i + len(sub_string))] == sub_string:
            count += 1

print(count)

"""
OUTPUT:
>>> enter a sub string: hello
3
"""
