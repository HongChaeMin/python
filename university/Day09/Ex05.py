def ctofahrenhite(cels):
    return cels * 9 / 5 + 32

def ftocelsius(fahr):
    return fahr - 32 * 5 / 9

for cels in range(28, 35, 2):
    print(f'섭씨: {cels}, 화씨: {ctofahrenhite(cels)}')

for fahr in range(90, 103, 3):
    print(f'섭씨: {ftocelsius(fahr)}, 화씨: {fahr}')

