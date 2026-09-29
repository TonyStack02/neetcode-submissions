class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set= set(nums)
        longest = 0
        for num in nums_set:
            if num-1 not in nums_set:
                counter = 1
                trovato = True
                while trovato:
                    if num+1 in nums_set:
                        num = num+1
                        counter = counter + 1
                    else:
                        trovato = False
                        if counter>longest:
                            longest=counter
        return longest