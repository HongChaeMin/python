sum = 0
for i in 1.1, 2.5, 3.6, 4.2, 5.4:
    sum += i
    print(i, sum)
else:
    print("합 : %.2f, 평균 : %.2f" % (sum, sum / 5))

for i in range(3):
    coffee = input("주문하세요: [아메리카노] [카페라떼] [카푸치노] >> ")
    if coffee == "아메리카노":
        print(coffee, "주문")
    elif coffee == "카페라떼":
        print(coffee, "주문")
    elif coffee == "카푸치노":
        print(coffee, "주문")
    else:
        print("모르겠어요")
else:
    print("주문을 마치겠습니다")

n = input("10진수의 한 자릿수 입력 >> ")
print("두 자릿수 정수에서 최소 한 자릿수가 %s인 정수 찾기 : " % n)
print(" 결과 ".center(50, '='))

for i in range(10, 100):
    snum = str(i)
    if n in snum:
        print(i, end=" ")
