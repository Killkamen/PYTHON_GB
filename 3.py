def is_prime():
    num = int(input("Введите число: "))

    if num < 0 or num > 100000:
        print "Введено недопустимое число. Допустимы числа от 0 до 100000."

    if num == 1 or num == 0:
        print "Число не является ни простым, ни составным."

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print "Число составное."
    print "Число простое."

print(is_prime())
