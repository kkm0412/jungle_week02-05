from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        files = deque(list(path.split("/")))
        current_path = ["/"]
        current_path = deque(files.popleft())
        for file in files:
            if file == (".."):
                current = current_path.pop()
                if current == "/":
                    current_path.append(current)
            else:
                current_path.append(file)
        return current
    # return current_path

# paths = input().split()
inputs = deque(input().split(' '))
inputs.popleft() #path
inputs.popleft() #"="
# inputs.remove('"')
# print(inputs)
path_input = inputs.pop()
paths = Solution()
paths.simplifyPath(path_input)
# paths = 
#""