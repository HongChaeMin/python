from random import randint

randomNumber = randint(1, 10)

inputNumber = int(input("1에서 10 사이의 수를 맞히세요 >> "))
while True:
    if randomNumber < inputNumber:
        inputNumber = int(input("{} 보다 더 작은 수로 다시 입력 >> ".format(inputNumber)))
    elif inputNumber < randomNumber:
        inputNumber = int(input("{} 보다 더 큰 수로 다시 입력 >> ".format(inputNumber)))
    else:
        print("축하드립니다", inputNumber, "정답입니다")
        break
