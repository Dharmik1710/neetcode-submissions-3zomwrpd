class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(chr(len(s)))
            result.append(s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        i = 0
        while(i < len(s)):
            print(s[i])
            size = ord(s[i])
            i+=1
            j = i
            ns = []
            while(j < min(i + size, len(s))):
                ns.append(s[j])
                j+=1
            i=j
            print("".join(ns))
            result.append("".join(ns))
        return result