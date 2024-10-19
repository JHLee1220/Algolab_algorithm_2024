#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int dx[8] = {-2, -1, 1, 2, 2, 1, -1, -2};
int dy[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int board[8][8], visited[8][8];
int m, n, T;

struct Move {
    int x, y, degree;
    Move(int _x, int _y, int _degree) : x(_x), y(_y), degree(_degree) {}
};

bool isValid(int x, int y) {
    return (x >= 0 && x < m && y >= 0 && y < n && visited[x][y] == 0);
}

int getDegree(int x, int y) {
    int degree = 0;
    for (int i = 0; i < 8; i++) {
        int nx = x + dx[i], ny = y + dy[i];
        if (isValid(nx, ny)) {
            degree++;
        }
    }
    return degree;
}

bool solve(int sx, int sy) {
    visited[sx][sy] = 1;
    int x = sx, y = sy;

    for (int mc = 2; mc <= m * n; mc++) {
        vector<Move> c;

        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (isValid(nx, ny)) {
                c.push_back(Move(nx, ny, getDegree(nx, ny)));
            }
        }

        if (c.empty()) {
            return false;
        }

        sort(c.begin(), c.end(), [](Move a, Move b) {
            return a.degree < b.degree;
        });

        x = c[0].x;
        y = c[0].y;
        visited[x][y] = mc;
    }

    return true;
}

int main() {
    cin >> T;
    while (T--) {
        int a, b;
        cin >> m >> n >> a >> b;
        memset(visited, 0, sizeof(visited));
        if (solve(a - 1, b - 1)) {
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
