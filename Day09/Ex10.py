def myKeyPrint(**kwargs):
    for key in kwargs:
        print(f'{key} : {kwargs[key]}')

myKeyPrint(여자친구=6, 마마무=4)
myKeyPrint(엑소=9, 트와이스=9, 블랙핑크=4, 방탄소년단=7)

coffeePrice = {'에스프레소' : 2500, '아메리카노' : 2800, '카페라떼' : 3200}
myCar = {"brand" : "현대", "model" : "제네시스", "year" : 2016}
myKeyPrint(**coffeePrice)
myKeyPrint(**myCar)
