import heapq

# 4*4的数字华容道AI

class PuzzleSolver:
    def __init__(self):
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]
        self.directions = ['D', 'U', 'R', 'L']
        self.hs = 0
        self.turning_factor = 1.25  # 设为1.00时不额外增加转角因子，为最精确最短路径，该因子越大计算越快，也越不精准。最大推荐值为1.25
        self.linear_factor = 9.00  # 设为0时不额外增加线性冲突因子，为最精确最短路径，该因子越大计算越快，也越不精准。最大推荐值为9.00

    def solve(self, board):
        n = 4
        target = "123456789ABCDEF0"
        start = self.board_to_string(board, n)

        heap = [(self.get_heuristic(start, target, n), 0, start, '')]
        visited = set()
        heapq.heapify(heap)

        while heap:
            _, steps, current, path = heapq.heappop(heap)

            if current == target:
                return path

            if current in visited:
                continue

            visited.add(current)

            zero_pos = current.index('0')
            x, y = divmod(zero_pos, n)

            for i in range(4):
                new_x, new_y = x + self.dx[i], y + self.dy[i]
                new_pos = new_x * n + new_y
                if 0 <= new_x < n and 0 <= new_y < n:
                    new_state = self.swap(current, zero_pos, new_pos)
                    if new_state not in visited:
                        new_cost = self.get_heuristic(new_state, target, n) + steps + 1
                        heapq.heappush(heap, (new_cost, steps + 1, new_state, path + self.directions[i]))

        return "No solution"

    def get_heuristic(self, state, target, n):
        self.hs += 1
        heuristic = 0
        for i, char in enumerate(state):
            if char != '0':
                target_idx = target.index(char)
                current_row, current_col = divmod(i, n)
                target_row, target_col = divmod(target_idx, n)

                row_distance = abs(current_row - target_row)
                col_distance = abs(current_col - target_col)
                distance = row_distance + col_distance

                if row_distance > 0 and col_distance > 0:
                    distance *= self.turning_factor

                heuristic += distance

        if heuristic > 10:
            linear_conflict = 0
            for row in range(n):
                for col1 in range(n):
                    for col2 in range(col1 + 1, n):
                        idx1 = row * n + col1
                        idx2 = row * n + col2
                        if state[idx1] != '0' and state[idx2] != '0':
                            target_idx1 = target.index(state[idx1])
                            target_idx2 = target.index(state[idx2])
                            target_row1, target_col1 = divmod(target_idx1, n)
                            target_row2, target_col2 = divmod(target_idx2, n)

                            if target_row1 == row and target_row2 == row and target_col1 > target_col2:
                                linear_conflict += 1

            for col in range(n):
                for row1 in range(n):
                    for row2 in range(row1 + 1, n):
                        idx1 = row1 * n + col
                        idx2 = row2 * n + col
                        if state[idx1] != '0' and state[idx2] != '0':
                            target_idx1 = target.index(state[idx1])
                            target_idx2 = target.index(state[idx2])
                            target_row1, target_col1 = divmod(target_idx1, n)
                            target_row2, target_col2 = divmod(target_idx2, n)

                            if target_col1 == col and target_col2 == col and target_row1 > target_row2:
                                linear_conflict += 1

            heuristic += linear_conflict * self.linear_factor

        return heuristic

    @staticmethod
    def swap(s, i, j):
        chars = list(s)
        chars[i], chars[j] = chars[j], chars[i]
        return ''.join(chars)

    @staticmethod
    def board_to_string(board, n):
        return ''.join(hex(num)[2:].upper() if num != 0 else '0' for row in board for num in row)

def ai(board):  # 传入4*4的二维数组
    solver = PuzzleSolver()

    print("开始计算...")
    solution = solver.solve(board)

    print(f"解法：{solution}")
    print(f"步数：{len(solution)}")
    print(f"广度：{solver.hs}")
    return solution
