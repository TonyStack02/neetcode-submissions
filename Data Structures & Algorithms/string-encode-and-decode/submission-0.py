class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(str(len(string)))
            encoded.append('#')

        encoded.append('-')
        
        for string in strs:
            encoded.append(string)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        
        dash_index = s.find('-')
        lengths_str = s[:dash_index]
        lengths = (int (x) for x in lengths_str.split('#') if x)

        word_str=s[dash_index+1:]

        start = 0
        for length in lengths:
            decoded.append(word_str[start:start+length])
            start = start + length
        return decoded