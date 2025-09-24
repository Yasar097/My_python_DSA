from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])

            # left part is sorted
            if nums[mid] >= nums[l]:
                res = min(res, nums[l])
                l = mid + 1
            else:  # right part is sorted
                r = mid - 1

        return res

