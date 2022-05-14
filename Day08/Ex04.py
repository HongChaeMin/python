from random import randrange
from random import sample

myLotto = set()
while True:
    num = randrange(1, 46)
    print(num, end = ' ')
    myLotto.add(num)
    if len(myLotto) == 6:
        break

print()
print('집합 : {}'.format(myLotto))
print('정렬 리스트 : {}'.format(sorted(myLotto)))
print()

lotto = sample(range(1, 46), 6)
print('sample function list : {}'.format(lotto))
print('sample function sorted list : {}'.format(sorted(lotto)))

