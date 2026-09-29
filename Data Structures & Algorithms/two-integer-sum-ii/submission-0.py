class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers)-1

        while(i<j):
            numbers_sum= numbers[i]+numbers[j]
            if numbers_sum > target:
                j-=1
            elif numbers_sum < target:
                i+=1
            else:
                return [i+1,j+1]