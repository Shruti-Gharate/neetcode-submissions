class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += word + "#" + str(len(word))
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = len(s) -1 

        while i > 0:
            j = i

            while s[j] != "#":
                j -=1

            length = int(s[j+1:i+1])
            word = s[j - length: j]
            result.append(word)
            i = j - length - 1
        return result[::-1]
# class Solution:
#     def encode(self, strs: List(str)) -> str:
#         res = ""
#         for string in strs:
#             res += string + "\x1f"
#         return res
#     def decode(self, s: str) -> List[str]:
#         return s.split("\x1f")[:-1]
            

