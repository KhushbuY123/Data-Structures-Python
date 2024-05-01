def Print_digit(num):
    if num == 0:
        return
    digit = num % 10
    Print_digit(num // 10)
    print(digit, end="")

num = 134
Print_digit(num)
