# divmod() : 반환 값이 2개 (몫과 나머지)

data = divmod(28, 9)
print(data[0]) # 3
print(data[1]) # 1

d1, d2 = divmod(28, 9)
print(d1) # 3
print(d2) # 1

# bin() : 10진수를 2진수 문자열 반환
# oct() : 10진수를 8진수 문자열 반환
# hex() : 10진수를 16진수 문자열 반

# int('진수문자열', 진법 기수)
# int ('0b11', 0) : 2진수
# int ('0o11', 0) : 8진수
# int ('0x11', 0) : 16진수

planet = input('원하는 행성은? ')
strRadius = input(planet + ' 반지름은? ')
radius = int(strRadius)

length = 2 * 3.14 * radius
print(planet, '반지름 : ', radius)
print(planet, '둘레길이 : ', length)

# data = int(input('정수 입력 >> '))

# print('2진수', bin(data));
# print('8진수', oct(data));
# print('10진수', data);
# print('16진수', hex(data));


# 20222422 홍채민 lab1
num1 = float(input("첫 번째 수 입력 >> "))
num2 = float(input("두 번째 수 입력 >> "))
print("합 : ", num1 + num2)
print("차 : ", num1 - num2)
print("곱하기 : ", num1 * num2)
print("나누기 : ", num1 / num2)
expression = input('연산식 입력 (예 3.2 + 4 * 1.5) >> ')
print("연산식 : ", expression, "결과 : ", eval(expression))


# 20222422 홍채민 lab2
base = int(input("입력할 정수의 진수(base)는? "))
invar = input(str(base) + "진수 정수 입력 >> ")
data = int(invar, base)

print('2진수', bin(data));
print('8진수', oct(data));
print('10진수', data);
print('16진수', hex(data));

