class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += i
            ans += "."
        
        return ans
    def decode(self, s: str) -> List[str]:
        ans = s.split(".")
        ans.pop()
        return ans