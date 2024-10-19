dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def is_valid(x, y, m, n, visited):
    return 0 <= x < m and 0 <= y < n and visited[x][y] == 0

def solve(x, y, move_count, m, n, visited):
    if move_count == m * n:
        return True  # 모든 셀을 방문한 경우
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if is_valid(nx, ny, m, n, visited):
            visited[nx][ny] = move_count + 1
            if solve(nx, ny, move_count + 1, m, n, visited):
                return True
            visited[nx][ny] = 0  # 백트래킹
    return False

def main():
    T = int(input())
    for _ in range(T):
        m, n, a, b = map(int, input().split())
        visited = [[0] * n for _ in range(m)]
        visited[a - 1][b - 1] = 1  # 출발점
        if solve(a - 1, b - 1, 1, m, n, visited):
            print(1)
            for row in visited:
                print(" ".join(map(str, row)))
        else:
            print(0)

if __name__ == "__main__":
    main()
