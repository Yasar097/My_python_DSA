class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()   # keeps track of current sliding window
        L = 0            # left pointer

        for R in range(len(nums)):   # iterate with right pointer
            # if window size exceeds k, shrink from the left
            if R - L > k:
                window.remove(nums[L])
                L += 1

            # if duplicate found in current window, return True
            if nums[R] in window:
                return True

            # add current number into the window
            window.add(nums[R])

        return False
