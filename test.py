# ENUMERET
integers = [1, 2, 3, 4]
for element,index in enumerate(integers):
    print(f'{element}-{index}')
# all any
list = [0, 1, True]
print(all(list))
print(any(list))
print(all(e >0 for e in integers)) # Выведет True если все положительные