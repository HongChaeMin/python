value = input('실수(세 자리.두 자리로 345.78 처럼)를 하나 입력하세요 >> ')
num = value.replace('.', '')
sum = 0
sum += int(num[0])
sum += int(num[1])
sum += int(num[2])
sum += int(num[3])
sum += int(num[4])
print('입력값 :', value)
print('모든 자릿수 합 :', sum)

str = input('2개의 단어를 빈 공간으로 구분해 입력하세요 >>')
pos = str.find(' ')
preWord = str[:pos]
postWord = str[pos + 1:]
print(preWord, postWord)
print(preWord[::-1], postWord[::-1])

m, n, x, y = input('4개의 수 입력 >> ').split()
a, b, c, d = float(m), float(n), float(x), float(y)
print('입력값 :', a, b, c, d)
sum = a + b + c + d
print('합 :', sum, '평균 :', sum / 4)
print('최대 :', max(a, b, c, d), '최소 :', min(a, b, c, d))

