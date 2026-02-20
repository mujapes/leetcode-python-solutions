class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split(" ")
        reversed = ""
        for word in split:
            reversed += word[::-1] + " "
        return reversed[:-1]

# Runtime: 3 ms, Beats 59.27%
# Memory: 19.83 MB, Beats 41.75%
