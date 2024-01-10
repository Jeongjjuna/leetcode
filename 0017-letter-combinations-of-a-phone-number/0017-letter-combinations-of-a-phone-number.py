from collections import deque

class Solution:
    
    # 접근1. dfs
    def sol_1(self, digits):
        
        def dfs(digits, dep, curr_str): # s = ["2", "3"], pre = ["a, d"]
            if dep == len(digits):
                ans.append("".join(curr_str))
                return

            for nv in phone[digits[dep]]:
                curr_str.append(nv)
                dfs(digits, dep + 1, curr_str)
                curr_str.pop()
            
        
        # 변수 입력 및 선언
        ans = []
        phone = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]
        }
       
        # 입력값이 빈 문자열일 경우
        if digits == "":
            return ans
        
        dfs(digits, 0, [])
        return ans

    
    def letterCombinations(self, digits: str) -> List[str]:
        return self.sol_1(digits)

    
    
    
    
    
    