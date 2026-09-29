class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = set()
        for k in range(len(nums)):
            i=k+1
            j=len(nums)-1
            while i<j:
                current_sum= nums[i]+nums[j]+ nums[k]
                
                if current_sum > 0:
                    j-=1
                elif current_sum < 0:
                    i+=1
                else:
                    triples.add((nums[i], nums[j], nums[k]))     
                    i+=1
                    j-=1 

        return [list(t) for t in triples]       
