str = 'Hello python!'

n = len(str)
print('문자열', str, '길이', n)
print('첫 문자', str[0], str[-n])
print('가운데 문자', str[n//2], str[-n//2])
print('마지막 문자', str[n-1], str[-1])

str = 'Month Python'
len(str)

print(str[0:5], str[6:], str[6:12])
print(str[-12:-7], str[-6:], str[-6:0])

str = '일요일 기러기'
print(str[:3], str[4:]) # 양수 이용
print(str[:-4], str[-3:]) # 음수 이용
print(str[:], str[::], str[::1]) # 모든 문자열 참조
print(str[::2]) # 한 문자씩 건너뛰기
print(str[::3]) # 두 문자씩 건너뛰기
print(str[::-2]) # 역순으로 한 문자씩 건너뛰기
print(str[::-1]) # 역순으로 출력

