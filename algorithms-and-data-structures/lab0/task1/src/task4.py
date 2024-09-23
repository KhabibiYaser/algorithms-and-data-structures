def sum_ab2_file(path1, path2):
    file = open(path1)
    s = file.readline()
    a, b = map(int, list(s.split()))
    if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
        open(path2, "w").write(str(a + b ** 2))
    file.close() # закрытие файла

sum_ab2_file("input3.txt", "output3.txt")