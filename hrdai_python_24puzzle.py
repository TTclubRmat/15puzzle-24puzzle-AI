import heapq


# 5*5的数字华容道AI

class PuzzleSolver:
    def __init__(self):
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]
        self.directions = ['D', 'U', 'R', 'L']
        self.hs = 0

    def solve_beam(self, board):
        n = 5
        target = "123456789ABCDEFGHIJKLMNO0"
        start = self.board_to_string(board, n)
        beam_width = 1000  # 设置束宽度

        heap = [(self.get_heuristic_best(start, target, n), 0, start, '', [])]
        visited = set()
        heapq.heapify(heap)

        while heap:
            next_level = []
            for _ in range(min(len(heap), beam_width)):
                _, steps, current, path, manhattan_distances = heapq.heappop(heap)

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
                            new_manhattan_distance = self.get_heuristic_best(new_state, target, n)
                            new_manhattan_distances = manhattan_distances + [new_manhattan_distance]

                            new_cost = new_manhattan_distance + steps + 1
                            heapq.heappush(next_level, (
                                new_cost, steps + 1, new_state, path + self.directions[i], new_manhattan_distances))

            heap = next_level
            heapq.heapify(heap)

        return "No solution"

    def get_heuristic_best(self, state, target, n):
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

                heuristic += distance

        if self.hs % 100000 == 0:
            print(f" * * 计算中  当前广度：{self.hs}, 剩余曼哈顿步数{heuristic}")

        return heuristic

    @staticmethod
    def swap(s, i, j):
        chars = list(s)
        chars[i], chars[j] = chars[j], chars[i]
        return ''.join(chars)

    @staticmethod
    def board_to_string(board, n):
        def to_base_25(num):
            if num == 0:
                return '0'
            base_25 = ''
            while num > 0:
                remainder = num % 25
                if remainder < 10:
                    base_25 = chr(48 + remainder) + base_25  # 0-9
                else:
                    base_25 = chr(65 + remainder - 10) + base_25  # A-O
                num //= 25
            return base_25

        return ''.join(to_base_25(num) if num != 0 else '0' for row in board for num in row)


def ai(board):
    solver = PuzzleSolver()

    print("开始计算...")
    print(board)
    solution = solver.solve_beam(board)

    print(f"解法：{solution}")
    print(f"步数：{len(solution)}")
    print(f"广度：{solver.hs}")
    return solution


print("测试使用算法解5*5数字华容道")
board_5 = ((8, 13, 20, 16, 15), (1, 23, 0, 19, 24), (18, 11, 12, 7, 17), (6, 9, 2, 21, 14), (5, 10, 4, 22, 3))
ai(board_5)

# def solve_ida_star(self, board):
#     n = 5
#     target = "123456789ABCDEFGHIJKLMNO0"
#     start = self.board_to_string(board, n)
#
#     def ida_star(start_ida_star, target, n):
#         threshold = self.get_heuristic_best(start_ida_star, target, n)
#         while True:
#             temp = self.search(start_ida_star, target, 0, threshold, '', n)
#             if isinstance(temp, str):  # Found a solution
#                 return temp
#             if temp == float('inf'):
#                 return "No solution"
#             threshold = temp
#
#     return ida_star(start, target, n)
#
# def search(self, node, target, g, threshold, path, n):
#     f = (g + self.get_heuristic_best(node, target, n))
#     if f > threshold:
#         return f
#     if node == target:
#         return path
#
#     min_cost = float('inf')
#     zero_pos = node.index('0')
#     x, y = divmod(zero_pos, n)
#
#     for i in range(4):
#         new_x, new_y = x + self.dx[i], y + self.dy[i]
#         new_pos = new_x * n + new_y
#         if 0 <= new_x < n and 0 <= new_y < n:
#             new_state = self.swap(node, zero_pos, new_pos)
#             if new_state != node:  # Avoid revisiting the same state
#                 temp = self.search(new_state, target, g + 1, threshold, path + self.directions[i], n)
#                 if isinstance(temp, str):  # Found a solution
#                     return temp
#                 if temp < min_cost:
#                     min_cost = temp
#
#     return min_cost