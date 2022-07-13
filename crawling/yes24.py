from urllib.request import urlopen
from bs4 import BeautifulSoup

print("yes24의 국내 도서 종합 best seller web page 가져오기")

bookSize = 40
bookPage = 1
while True:
    print(f'현재 bookSize : {bookSize}, bookPage : {bookPage}')
    print('1. 검색할 책 개수 정하기(기본 40개)\t 2. 페이지 정하기(기본 1페이지)\t 3. 실행하기\t 4. 종료하기')
    number = int(input())
    if number == 1:
        bookSize = input('검색할 책 개수를 입력해주세요 > ')
    elif number == 2:
        bookPage = input('원하는 페이지를 입력해주세요 > ')
    elif number == 3:
        url = f"http://www.yes24.com/24/category/bestseller?categorynumber=001&sumgb=06&fetchsize={bookSize}&pagenumber={bookPage}"
        print(f"요청 url : {url}")

        # yes24의 국내 도서 종합 best seller web page 가져오기
        html = urlopen(url)
        bsObject = BeautifulSoup(html, "html.parser")

        # 책 제목 넣기
        # 책 상세 페이지 주소 추출해서 저장하기
        bookNameList = []
        bookPageLinkList = []
        for cover in bsObject.find_all('td', {'class': 'goodsTxtInfo'}):
            name = cover.find('a').get_text()
            bookNameList.append(name)
            link = "http://www.yes24.com" + cover.find('a').get('href')
            bookPageLinkList.append(link)

        # 작가, 출판사 넣기
        bookAuthorList = []
        bookPublisherList = []
        for cover in bsObject.find_all('div', {'class': 'aupu'}):
            author = cover.select('a')[0].get_text()
            bookAuthorList.append(author)
            publisher = cover.select('a')[1].get_text()
            bookPublisherList.append(publisher)

        # 책 가격 넣기
        bookPriceList = []
        for cover in bsObject.find_all('span', {'class', 'priceB'}):
            price = cover.get_text()
            bookPriceList.append(price)

        # 순위 넣기
        bookRankList = []
        for cover in bsObject.find_all('td', {'class': 'num'}):
            rank = cover.get_text()
            bookRankList.append(rank)

        for index in range(len(bookRankList)):
            print("{")
            print(f"  \"순위\" : \"{bookRankList[index]}\",")
            print(f"  \"제목\" : \"{bookNameList[index]}\",")
            print(f"  \"저자\" : \"{bookAuthorList[index]}\",")
            print(f"  \"출판사\" : \"{bookPublisherList[index]}\",")
            print(f"  \"가격\" : \"{bookPriceList[index]}\",")
            print(f"  \"상세 페이지\" : \"{bookPageLinkList[index]}\"")
            print("}," if index < bookSize - 1 else "}")
    else:
        print('프로그램을 종료합니다')
        break
