########## 1 ##########
str1 = input("문자열 1 : ")
str2 = input("문자열 2 : ")

print(str1, str2)

########## 2 ##########
speed = int(input("차의 속도를 입력 (km) : "))
print(speed, "(km)은 ", (speed / 1.61), "마일(miles)이다.")

########## 3 ##########
count = int(input("아메리카노 몇 개 주문하세요? : "))
print("총 가격은", (count * 3500), "원 이다.")

########## 4 ##########
print("알려진 지구 둘레 : 40120")
sameEarthRound = float(input("지구와 같은 원둘레 : "))

print("차이 :", (40120 - sameEarthRound), "(km)")

########## 5 ##########
celsius = int(input("온도 입력 >> "))
accurateCalculation = celsius * (9 / 5) + 32
abbreviatedCalculation = celsius * 2 + 30

print("정확 계산 : 섭씨 =", celsius, ", 화씨 =", accurateCalculation)
print("약식 계산 : 섭씨 =", celsius, ", 화씨 =", abbreviatedCalculation)
print("차이 :", accurateCalculation - abbreviatedCalculation)


########## 6 ##########
firstNumber = int(input("Enter First number : "))
secondNumber = int(input("Enter Second number : "))

print(firstNumber, "/", secondNumber, "==>", firstNumber / secondNumber)
print(firstNumber, "%", secondNumber, "==>", firstNumber % secondNumber)
print(firstNumber, "//", secondNumber, "==>", firstNumber // secondNumber)
print(firstNumber, "**", secondNumber, "==>", firstNumber ** secondNumber)


########## 7 ##########
firstNumber = float.fromhex(input("첫 번째 16진수 실수 입력 : "))
secondNumber = float.fromhex(input("두 번째 16진수 실수 입력 : "))

print("실수1 :", firstNumber, ", 실수2 :", secondNumber)
print("합 :", firstNumber + secondNumber)
print("차 :", firstNumber - secondNumber)
print("곱하기 :", firstNumber * secondNumber)
print("나누기 :", firstNumber / secondNumber)

########## 8 ##########
number = input("네 자리수 정수 입력 >> ")
print(number[3] + number[2] + number[1] + number[0])
