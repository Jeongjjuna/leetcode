from collections import deque

class Solution:
    
    def __init__(self):
        self.phone = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }
    
    def dfs(self, s, pre, ans): # s = ["2", "3"]
        if len(s) == 0:
            ans.append("".join(pre))
            return
        
        val = s.popleft()
        for nv in self.phone[val]:
            pre.append(nv)
            self.dfs(s, pre, ans)
            pre.pop()
            
        s.appendleft(val)

        
    # 접근1. dfs
    def letterCombinations(self, digits: str) -> List[str]:

        ans = []
        if digits == "":
            return ans
        else:
            self.dfs(deque(list(digits)), [], ans)
        
        return ans