import ctypes
import time

# 使用C语言动态链接库

# 选择束搜索宽度。宽度越大，时间越长，越准确。
# lib = ctypes.CDLL('libs/libszhrd_5_7000.dll')  # 束搜索宽度为7000，较快，在一些情况下接近于最短路径
lib = ctypes.CDLL('libs/libszhrd_5_50000.dll')  # 束搜索宽度为50000，较慢，接近于最短路径
# lib = ctypes.CDLL('libs/libszhrd_5_max.dll')  # 束搜索宽度为max，最慢，无限接近于最短路径

lib.cal.argtypes = [ctypes.POINTER(ctypes.c_int)]
lib.cal.restype = ctypes.c_char_p

input_str = input("输入：")  # 示例输入：12 15 1 0 5 2 17 14 7 13 11 8 16 10 4 3 6 9 23 18 21 22 20 19 24

array_1d = list(map(int, input_str.split()))
array_c = (ctypes.c_int * len(array_1d))(*array_1d)

print(array_1d)
print('计算...')

start_time = time.time()
result = lib.cal(array_c)
end_time = time.time()
result_decode = result.decode()
print("解法：", result_decode)
print(f"步数：{len(result_decode)}")
print(f"时间: {end_time - start_time} 秒")
