def sum_of_nums(s, trial):
    if trial == 2:
        print("Числа ушли диапазон -10^9 <= x,y <= 10^9 ")
    else:
        a, b = map(int, list(s.split()))
        if -10 ** 9 <= a <= 10 ** 9 and -10 ** 9 <= b <= 10 ** 9:
            return a + b
        else:
            print("Попробуй ввести число еще раз: ")
            sum_of_nums(input("nums: "), trial + 1)

print(sum_of_nums(input("nums: "), 0))

