class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        ans = right
        while(left <= right):
            k = (left + right) // 2
            ore_tot = 0
            for pila in piles: #stai provando a vedere se k va bene
                ore_tot += math.ceil(pila / k)
         
            
            if ore_tot > h:
                left = k + 1
            else:
                ans = k
                right = k - 1 
        return ans