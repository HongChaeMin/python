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
earthRound = int(input("알려진 지구 둘레 : "))
sameEarthRound = float(input("지구와 같은 원둘레 : "))

def circleRound(round) :
    return 2 * 3.141592 * (round / 2)

print("차이 : ", (circleRound(earthRound) - circleRound(sameEarthRound)), "(km)")
