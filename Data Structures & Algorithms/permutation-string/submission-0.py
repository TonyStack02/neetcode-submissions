class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1 

        s1_map = {}
        w_map = {}

        if len(s1) > len(s2):
            return False

        for i in range (len(s1)):
            if s1[i] in s1_map:
                s1_map[s1[i]] += 1
            else:
                s1_map[s1[i]] = 1

            if s2[i] in w_map:
                w_map[s2[i]] += 1
            else:
                w_map[s2[i]] = 1

        if s1_map == w_map:
                return True

        while right < len(s2) - 1:
            
            if s1_map == w_map:
                return True

            right += 1

            if s2[right] in w_map:
                w_map[s2[right]] += 1
            else:
                w_map[s2[right]] = 1
            
            if s2[left] in w_map and w_map[s2[left]] != 1:
                w_map[s2[left]] -= 1
            else:
                w_map.pop(s2[left], None)
            
            left += 1

        if s1_map == w_map:
                return True

        return False