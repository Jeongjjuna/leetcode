class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # temperatures에서 idx뒤에 값들중 온도가 올라가는 값까지의 거리
        def find(idx, temperatures):
            n = len(temperatures)
            for i in range(idx + 1, n):
                if temperatures[idx] < temperatures[i]:
                    return i - idx
            return 0
        
        
        # 접근1. 완전탐색 -> 시간초과 O(n**2)
        def sol_1(temperatures):
            answer = []
            n = len(temperatures)
            for i in range(n):
                answer.append(find(i, temperatures))
        
            return answer
        
        
        # dp -> 생각안남
        # 정렬 -> 생각안남
        # 접근2. 스택
        def sol_2(temperatures):
            n = len(temperatures)
            answer = [0] * n
            
            stack = [] # [(idx, tem)]
            
            for i in range(n):
                # 스택이 비었으면 집어넣는다.
                if len(stack) == 0:
                    stack.append((i, temperatures[i]))
                    continue
                
                
                while 0 < len(stack) and stack[-1][1] < temperatures[i]:
                    idx, val = stack.pop()
                    answer[idx] = i - idx
                stack.append((i, temperatures[i]))
                
            return answer
            
        
        return sol_2(temperatures)