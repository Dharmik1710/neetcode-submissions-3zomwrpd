class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(chr(len(s)))
            result.append(s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while(i < len(s)):
            size = ord(s[i])
            i+=1
            ns = []
            str_len = min(i + size, len(s))
            while(i < str_len):
                ns.append(s[i])
                i+=1
            result.append("".join(ns))
        return result