# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k
# долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# 3 2 4 -> yes 
# 3 2 1 -> no

m = int(input('Введите m размер шоколадки: '))
n = int(input('Введите n размер шоколадки: '))
k = int(input('Введите k сколько долек нужно отломать: '))
if k == m * n:
    print('Ничего ломать не нужно, жадина!')
elif (k%n == 0 or k%m == 0) and k < m * n:
    print('Yes')
else:
    print('NO')

