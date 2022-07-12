def hello(*names):
    for each in names:
        print(f'안녕, {each}')

hello('나타샤')
hello('수빈', '현수', '지효')
hello(*['방탄소년단', '블랙핑크'])
