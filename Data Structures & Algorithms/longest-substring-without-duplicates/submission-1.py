class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0 
        left = 0
        right = 0

        current_letters = set()

        for ch in s:
            
            if ch in current_letters:
                while s[left]!=ch:
                    current_letters.remove(s[left])
                    left += 1
                current_letters.remove(s[left])
                left += 1
            
            current_letters.add(ch)
            right += 1

            current_size = right - left
            if current_size > max_size:
                max_size = current_size

            

        return max_size
