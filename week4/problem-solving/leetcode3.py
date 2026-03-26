from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #일단은 visited한 곳은 -1로 설정
        #bfs 다 한 후에 1이 남아있는 곳에서 다시 진행
        result = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):   #전부 검사
                if grid[i][j] == "1":   #땅 발견시
                    queue.append((i, j))
                    while len(queue) != 0:
                        cur = queue.popleft()
                        y = cur[0]
                        x = cur[1]
                        if grid[y][x] == "1":   
                            grid[y][x] = "-1"#현재 땅은 -1로
                            if y - 1 >=0:   #상
                                queue.append((y-1, x))
                            if x - 1 >=0:   #좌
                                queue.append((y, x-1))
                            if y + 1 < len(grid):   #하
                                queue.append((y+1, x))
                            if x + 1 < len(grid[0]):    #우
                                queue.append((y, x+1))
                    result += 1
        return result
