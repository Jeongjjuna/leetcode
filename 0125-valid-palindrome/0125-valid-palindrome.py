class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Test
        #s = "abc ABC _ 0aZ"
        
        # 정규 표현식을 통해 원하는 문자만 골라서 리스트로 변환한다.
        regex = r'[a-zA-Z0-9]'
        result = re.findall(regex, s)
        
        # 문자중 모든 대문자를 소문자로 변환한다. # O(n)
        for i in range(len(result)):
            elem = result[i]
            if elem.isupper():
                result[i] = elem.lower()

        # 팬린드롬인지 확인한다. # O(n)
        n = len(result)
        for i in range(n//2):
            if result[i] != result[n-1-i]:
                return False
        return True