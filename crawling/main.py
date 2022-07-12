from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

print("================================")
print("웹 문서 전체 가져오기")
print(bsObject)
print("================================")
print("타이틀 가져오기")
print(bsObject.head.title)
print("================================")
print("모든 메타 데이터의 내용 가져오기")
for meta in bsObject.head.find_all('meta'):
    print(meta.get('content'))
print("================================")
print("모든 링크의 텍스트와 주소 가져오기")
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))
print("================================")

html = urlopen("https://www.python.org/about")
bsObject = BeautifulSoup(html, "html.parser")

print("원하는 태그의 내용 가져오기")
print(bsObject.head.find("meta", {"name": "description"}).get('content'))
