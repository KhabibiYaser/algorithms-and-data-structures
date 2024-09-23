import time

def fib_number2(n):
    if 0 <= n <= 10 ** 7:
        a, b = 0, 1
        for i in range(n):
            a, b = b % 10, (a + b) % 10
        return a





# t_start = time.perf_counter()
#
# file_input = open("input.txt")
# n = int(file_input.readline())
#
# t_start = time.perf_counter()
# num = fib_number2(n) % 10
# print("Время работы: %s секунд" % (time.perf_counter() - t_start))
#
# file_output = open("output.txt", "w")
# file_output.write(str(num))
#
# file_output.close()