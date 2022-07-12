from urllib.request import urlopen
from bs4 import BeautifulSoup

# yes24의 best seller web page 가져오기
html = urlopen("http://www.yes24.com/24/Category/BestSeller")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject)

# 책 상세 페이지 주소 추출해서 저장하기
bookPageLinkList = []
for cover in bsObject.find_all('p', {'class': 'copy'}):
    link = "http://www.yes24.com" + cover.select('a')[0].get('href')
    bookPageLinkList.append(link)

# 책 제목 넣기
bookNameList = []
for cover in bsObject.find_all('p', {'class': 'image'}):
    name = cover.select('img')[0].get('alt')
    bookNameList.append(name)

# 작가, 출판사 넣기
bookAuthorList = []
bookPublisherList = []
for cover in bsObject.find_all('p', {'class': 'aupu'}):
    author = cover.select('a')[0].get_text()
    bookAuthorList.append(author)
    publisher = cover.select('a')[1].get_text()
    bookPublisherList.append(publisher)

# 책 가격 넣기
bookPriceList = []
for cover in bsObject.find_all('p', {'class', 'price'}):
    price = cover.find('strong').get_text()
    bookPriceList.append(price)

for index in range(len(bookNameList)):
    print("{")
    print(f"  \"순위\" : \"{index}\"")
    print(f"  \"제목\" : \"{bookNameList[index]}\"")
    print(f"  \"저자\" : \"{bookAuthorList[index]}\"")
    print(f"  \"출판사\" : \"{bookPublisherList[index]}\"")
    print(f"  \"가격\" : \"{bookPriceList[index]}\"")
    print(f"  \"상세 페이지\" : \"{bookPageLinkList[index]}\"")
    print("}")
