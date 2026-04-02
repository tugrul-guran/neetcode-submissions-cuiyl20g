class Solution:

    def encode(self, strs: List[str]) -> str:

        result = ""

        for s in strs:
            l = len(s)
            code = str(l) + "#"
            result += code + s

        return result

    def decode(self, s: str) -> List[str]:

        result = []

        l = len(s)
        index = 0
        num = ""
        while index < l:
            char = s[index]

            if char != "#":
                num += char
                index += 1
            else:
                new = ""
                loop_count = int(num)
                index += 1
                for _ in range(loop_count):
                    new += s[index]
                    index += 1
                result.append(new)
                num = ""
          
        return result