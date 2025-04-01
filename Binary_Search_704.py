# Time:   O(log n)
# Space:  O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums)

        while left < right:
            central = left + (right-left)//2
            if nums[central] > target:
                right = central
            elif nums[central] < target:
                left = central + 1
            else:
                return central
            
        return -1