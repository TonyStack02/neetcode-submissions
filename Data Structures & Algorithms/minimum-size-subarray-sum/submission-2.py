class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0

        min_length = len(nums) 
        current_sum = 0
        found = False

        while right < len(nums):
            current_sum += nums[right]

            while current_sum >= target and left <= right:
                found = True
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                current_sum -= nums[left]
                left += 1
            
            right += 1
        
        if found:
            return min_length
        else:
            return 0