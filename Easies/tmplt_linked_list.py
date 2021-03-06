#
#   Date - 01.02.2022
#
#
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#       Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
#       Example 2:
# Input: nums = [0]
# Output: [0]
#
#
#       Constraints:
#     1 <= nums.length <= 104
#     -231 <= nums[i] <= 231 - 1

import timeit
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_list_node(nums: List[int]) -> 'ListNode':
        if not nums:
            return ListNode()
        tail = ListNode(nums[-1])
        for num in reversed(nums[:-1]):
            new_tail = ListNode(num, tail)
            tail = new_tail
        return tail

    def __eq__(self, other: List[int]):
        temp = self
        if not other: return temp.next is None
        for x in other:
            if x == temp.val:
                try:
                    temp = temp.next
                except:
                    return False
            else:
                return False
        return True

    def __repr__(self):
        tail: ListNode = self
        res: List[str] = []
        max_repe_len = 30  # in case of loops in linked list ..
        while tail and max_repe_len:
            res.append(str(tail.val))
            tail = tail.next
            max_repe_len -= 1
        return ' --> '.join(res)


def to_list(ln: Optional[ListNode]) -> List[int]:
    l = []
    while ln:
        l.append(ln.val)
        ln = ln.next
    return l


class Solution:
    def some_function(self, nums: Optional['ListNode']) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        print(f'nums: {nums}')


def testing():
    sol = Solution()

    nums = [0, 1, 0, 3, 12]
    res = sol.some_function(ListNode.create_list_node(nums))
    assert ([1, 3, 12, 0, 0] == res)

    nums = [0]
    res = sol.some_function(ListNode.create_list_node(nums))
    assert ([0] == res)

    nums = [0, -1]
    res = sol.some_function(ListNode.create_list_node(nums))
    assert ([-1, 0] == res)

    nums = [0, 0]
    res = sol.some_function(ListNode.create_list_node(nums))
    assert ([0, 0] == res)


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" % (
        timeit.timeit(testing, number=100)))
