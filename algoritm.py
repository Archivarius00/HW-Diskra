n = int(input('Введите количество желаемых списков: '))
arr = []

for k in range(n):
    if k != 0:
        arr = lst
        list1 = [str(inp) for inp in input().split()]
        lst = list(set(list1) & set(arr))
    else:
        list1 = [str(inp) for inp in input().split()]
        lst = list1

arr = lst
ans = ' '.join(lst)

print(f"Вот пересечение всех множеств: {{{ans}}}")