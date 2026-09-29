class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] <= nums[right]: #se non è ruotato
            return nums[left]

        while left <= right: 
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]: 
                return nums[mid + 1]
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1