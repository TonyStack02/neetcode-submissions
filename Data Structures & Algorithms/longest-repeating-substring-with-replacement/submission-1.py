class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right = 0
        left = 0
        ch_map = {}
        longest = 0
        while right < len(s):

            #adding the ch to the hash map
            if s[right] not in ch_map:
                ch_map[s[right]] = 1
            else:
                ch_map[s[right]] += 1


            while (right - left + 1) - max((ch_map).values()) - k > 0:
                ch_map[s[left]] -= 1
                left += 1
                
            
            longest = max(longest, right - left + 1)
            right += 1

        return longest