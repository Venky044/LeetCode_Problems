# Merge Two Sorted Lists

"""
    you are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists in a One sorted list. 
    The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.

    Input : list1 = [1,2,4], list2 = [1,3,4]
    Output : [1,1,2,3,4,4]

    Input : list1 = [], list2 = []
    Output : []

    Input : list1 = [], list2 = [0]
    Output : [0]
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def mergeTwoLists(self, list1, list2):
        if len(list1) > 0:
            for i in list1:
                new_node = Node(i)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                self.length += 1
        else:
            return list2

        # temp = self.head
        # while temp:
        for i in list2:
            new_node = Node(i)
            temp = self.head
            while temp:
                if i >= temp.val and i <= temp.next.val:
                    new_node.next = temp.next
                    temp.next = new_node
                    self.length += 1
                    break
                temp = temp.next

        # def prin(self):
        #     temp = self.head
        #     while temp:
        #         print(temp.val)
        #         temp = temp.next

        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next


li1 = [1, 2, 4]
li2 = [1, 3, 4]

# li1 = []
# li2 = [0]

sor = Solution()
# print(sor.mergeTwoLists(li1, li2))


# --------------------------------------------------------------------------


# normal merge sort solution for above QST
def fun(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    out_list = []

    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            out_list.append(l1[i])
            i += 1
        else:
            out_list.append(l2[j])
            j += 1

    while i < len(l1):
        out_list.append(l1[i])
        i += 1

    while j < len(l2):
        out_list.append(l2[j])
        j += 1

    return out_list


# list1 = [1, 2, 4]
# list2 = [1, 3, 4]

# list1 = []
# list2 = [0]

# print(fun(list1, list2))
