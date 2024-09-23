def sum_of_nums(s, trial):
    if trial == 2:
        print("Числа ушли за диапазон !( ")
    else:
        a, b = map(int, list(s.split()))
        if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= a <= 10 ** 9:
            return a + b ** 2
        else:
            print("Попробуй ввести число еще раз: ")
            sum_of_nums(input(), trial + 1)

print(sum_of_nums(input("nums: "), 0))