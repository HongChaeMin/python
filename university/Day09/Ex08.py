def addOne():
    global i
    print(f'\t 전역 변수 i 읽기, i + 1 : {i + 1}')
    i += 1

i = 20
print(f'i = {i}')
addOne()
print(f'i = {i}')
