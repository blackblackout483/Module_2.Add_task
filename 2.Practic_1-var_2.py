def ancient_code(number):
    result = ''
    for i in range(1, number):
        for j in range(1, number):
            if n % (i + j) == 0 and (i != j) and i < j:
                result += str(i) + str(j)

    return result


n = int(input('Введите число: '))

password = ancient_code(n)
print(f'Пароль числа {n}:', password)

