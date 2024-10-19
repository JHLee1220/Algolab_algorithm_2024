#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int dx[8] = {-2, -1, 1, 2, 2, 1, -1, -2};
int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int board[8][8], visited[8][8];
int m, n, t;

bool isValid(int x, int y) {
    return (x >= 0 && x < m && y >= 0 && y < n && visited[x][y] == 0);
}

bool solve(int x, int y, int moveCount) {
    if (moveCount == m * n) return true;  // 모든 셀을 방문한 경우
    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if (isValid(nx, ny)) {
            visited[nx][ny] = moveCount + 1;
            if (solve(nx, ny, moveCount + 1)) return true;
            visited[nx][ny] = 0;  // 백트래킹
        }
    }
    return false;
}

int main() {
    cin >> t;
    while (t--) {
        int a, b;
        cin >> m >> n >> a >> b;
        memset(visited, 0, sizeof(visited));
        visited[a - 1][b - 1] = 1;  // 출발점
        if (solve(a - 1, b - 1, 1)) {
            cout << 1 << endl;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    cout << visited[i][j] << " ";
                }
                cout << endl;
            }
        } else {
            cout << 0 << endl;
        }
    }
    return 0;
}
