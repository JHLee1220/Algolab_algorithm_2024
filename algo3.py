T = int(input())

def tile(board, n, x, y, hx, hy, tn):
    if n == 2:
        # 2x2 격자의 경우 구멍난 셀을 제외하고 트로미노를 채움
        for i in range(2):
            for j in range(2):
                if (x + i, y + j) != (hx, hy):
                    board[x + i][y + j] = tn
        return tn + 1

    # 중앙 부분에 트로미노 배치
    mx, my = x + n // 2, y + n // 2
    if hx < mx and hy < my:
        # 구멍이 좌상단에 있는 경우
        board[mx - 1][my] = board[mx][my - 1] = board[mx][my] = tn
        tn += 1
        tn = tile(board, n // 2, x, y, hx, hy, tn)  # 좌상단
        tn = tile(board, n // 2, x, my, mx - 1, my, tn)  # 우상단
        tn = tile(board, n // 2, mx, y, mx, my - 1, tn)  # 좌하단
        tn = tile(board, n // 2, mx, my, mx, my, tn)  # 우하단
    elif hx < mx and hy >= my:
        # 구멍이 우상단에 있는 경우
        board[mx - 1][my - 1] = board[mx][my - 1] = board[mx][my] = tn
        tn += 1
        tn = tile(board, n // 2, x, y, mx - 1, my - 1, tn)  # 좌상단
        tn = tile(board, n // 2, x, my, hx, hy, tn)  # 우상단
        tn = tile(board, n // 2, mx, y, mx, my - 1, tn)  # 좌하단
        tn = tile(board, n // 2, mx, my, mx, my, tn)  # 우하단
    elif hx >= mx and hy < my:
        # 구멍이 좌하단에 있는 경우
        board[mx - 1][my - 1] = board[mx - 1][my] = board[mx][my] = tn
        tn += 1
        tn = tile(board, n // 2, x, y, mx - 1, my - 1, tn)  # 좌상단
        tn = tile(board, n // 2, x, my, mx - 1, my, tn)  # 우상단
        tn = tile(board, n // 2, mx, y, hx, hy, tn)  # 좌하단
        tn = tile(board, n // 2, mx, my, mx, my, tn)  # 우하단
    else:
        # 구멍이 우하단에 있는 경우
        board[mx - 1][my - 1] = board[mx - 1][my] = board[mx][my - 1] = tn
        tn += 1
        tn = tile(board, n // 2, x, y, mx - 1, my - 1, tn)  # 좌상단
        tn = tile(board, n // 2, x, my, mx - 1, my, tn)  # 우상단
        tn = tile(board, n // 2, mx, y, mx, my - 1, tn)  # 좌하단
        tn = tile(board, n // 2, mx, my, hx, hy, tn)  # 우하단

    return tn

def solve(n, hx, hy):
    # 격자판 생성
    board = [[-1 for _ in range(n)] for _ in range(n)]
    # 구멍난 부분 설정
    board[hx][hy] = 0
    # 트로미노 타일링
    tile(board, n, 0, 0, hx, hy, 1)

    # 결과 출력
    for row in board:
        print(" ".join(map(str, row)))

for _ in range(T):
    n = int(input())
    hx, hy = map(int, input().split())
    solve(n, hx, hy)
