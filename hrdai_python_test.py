import hrdai_python_15puzzle
import hrdai_python_24puzzle

print("测试使用算法解4*4数字华容道")
board_4 = ((14, 11, 8, 10), (3, 13, 4, 12), (2, 0, 15, 6), (1, 7, 5, 9))
hrdai_python_15puzzle.ai(board_4)

print("")

print("测试使用算法解5*5数字华容道")
board_5 = ((8, 13, 20, 16, 15), (1, 23, 0, 19, 24), (18, 11, 12, 7, 17), (6, 9, 2, 21, 14), (5, 10, 4, 22, 3))
hrdai_python_24puzzle.ai(board_5)
