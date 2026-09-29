class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Pre-allocate both lists with 1s matching the length of nums.
        # This prevents 'IndexError' when accessing indices directly.
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        # Initialize the first prefix value with the first element of nums.
        prefix[0] = nums[0]
        # Build prefix products: each position is the previous product times the current num.
        for i in range(1, len(nums)):
            # Multiply previous cumulative product with nums[i].
            prefix[i] = prefix[i - 1] * nums[i]
            
        # Initialize the last suffix value with the last element of nums.
        suffix[len(nums) - 1] = nums[len(nums) - 1]
        # Build suffix products from right to left (ending at index 0).
        for i in range(len(nums) - 2, -1, -1):
            # Multiply next cumulative product with nums[i].
            suffix[i] = suffix[i + 1] * nums[i]
            
        # Combine prefix and suffix values.
        # Using a new result list avoids overwriting elements in nums while reading them.
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                # First element only has elements to its right.
                res[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                # Last element only has elements to its left.
                res[i] = prefix[i - 1]
            else:
                # Middle elements multiply left prefix by right suffix.
                res[i] = prefix[i - 1] * suffix[i + 1]

        return res