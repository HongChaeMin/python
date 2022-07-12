word = list('삶꿈성')
word.extend('복빛')
print(word)

fruit = ['복숭어', '자두', '골드키위', '귤']
print(fruit)
fruit.sort(reverse=True)
print(fruit)

mix = word + fruit
print(sorted(mix))
print(sorted(mix, reverse=True))


