from random import sample

winNum = set()

def buyAutoLotto():
    lotto = []
    for i in range(5):
        num6 = set(sample(list(range(1, 46)), 6))
        lotto.append(num6)
    return lotto

def printNums(nums):
    for num in sorted(nums):
        print('%2d' % num, end = ' ')
    print()
