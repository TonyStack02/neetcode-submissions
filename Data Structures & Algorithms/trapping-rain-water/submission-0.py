class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1

        picco_i = False
        picco_j = False
        
        tot_area = 0

        while i<j: 

            if picco_i and picco_j:
                if h_picco_i < h_picco_j:
                    i+=1
                    if height[i] < h_picco_i:
                        tot_area += h_picco_i - height[i]
                    else:
                        h_picco_i = height[i]
                else: 
                    j-=1
                    if height[j] < h_picco_j:
                        tot_area += h_picco_j - height[j]
                    else:
                        h_picco_j = height[j]     

            else:
                if not picco_i:
                    if i!=0:
                        if height[i] >= height[i-1] and height[i] > height[i+1]:
                            picco_i=True
                            h_picco_i = height[i]
                        else:
                            i+=1
                    else:
                        if height[i] > height[i+1]:
                            picco_i=True
                            h_picco_i = height[i]
                        else:
                            i+=1

                if not picco_j:
                    if j != len(height)-1:
                        if height[j] > height[j-1] and height[j] >= height[j+1]:
                            picco_j=True
                            h_picco_j = height[j]
                        else:
                            j-=1
                    else:
                        if height[j] > height[j-1]:
                            picco_j=True
                            h_picco_j = height[j]
                        else:
                            j-=1

        return tot_area
        