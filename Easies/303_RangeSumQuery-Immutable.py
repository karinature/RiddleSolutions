#
#   Date - 18.05.2022
#
#
# 303. Range Sum Query - Immutable
# Easy
#
# Given an integer array nums, handle multiple queries of the following type:
#
#     Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
#
# Implement the NumArray class:
#
#     NumArray(int[] nums) Initializes the object with the integer array nums.
#     int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
#
#
#
# Example 1:
#
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
#
#
#
# Constraints:
#
#     1 <= nums.length <= 104
#     -105 <= nums[i] <= 105
#     0 <= left <= right < nums.length
#     At most 104 calls will be made to sumRange.
#


from math import prod
import timeit
from typing import List, Optional, Set, Dict
from collections import defaultdict


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums: List[int] = [0]
        temp = 0
        for n in nums:
            temp += n
            self.nums.append(temp)

    #     todo there's a slighty better way (no need in temp value)

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right + 1] - self.nums[left]


def testing():
    # Your NumArray object will be instantiated and called as such:
    obj = NumArray([-2, 0, 3, -5, 2, -1])

    result = obj.sumRange(0, 2)
    # print(f"result: {result}")
    assert (1 == result)

    result = obj.sumRange(2, 5)
    # print(f"result: {result}")
    assert (-1 == result)

    result = obj.sumRange(0, 5)
    # print(f"result: {result}")
    assert (-3 == result)

    pass


if __name__ == '__main__':
    print("\n Finished in --- %.5f seconds ---" %
          (timeit.timeit(testing, number=100)))
