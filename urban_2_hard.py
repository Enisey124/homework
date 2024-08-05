def passwort(q):
    couple = ''
    for i in range (1, q):
        for j in range (i + 1, q):
            if q % (i+j) == 0:
                couple += f"{i}{j}"
    return couple

number = 0
while number < 3 or number > 20:
    number = int(input("Введите число из первого поля (от 3 до 20): "))
ready_password = passwort(number)
print("Число для второго поля: ", ready_password)
print()
print()
print()
print()

print('Все пароли:')
end = 21
for n in range(3,end):
   result = str()
   for i in range(1,end):
        for j in range(i+1,end):
           if n % (i + j) == 0:
              result += f"{i}{j}"
   print (f'{n} - {result}')