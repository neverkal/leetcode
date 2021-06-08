import collections

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = collections.defaultdict(str)
        d["{"] = "}"
        d["["] = "]"
        d["("] = ")"

        for ch in s:
            print(stack)
            if stack and d[stack[-1]] == ch:
                # 스택에 값이 있고 들어온 문자가 스택에 쌓인 괄호와 쌍일 경우 stack pop
                stack.pop()
            else:
                # 없는 괄호면 추가
                stack.append(ch)

        # 스택에 값이 없다면 성공 있으면 실패
        return not stack


sol = Solution()
print(sol.isValid(s="([)]"))
